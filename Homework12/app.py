from flask import Flask, render_template, request
import requests
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data_test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/")
def form():
    return render_template('form.html')


@app.route("/result", methods=['POST'])
def result():
    from models import Point
    zip_code = request.form['zip']
    key = 'AIzaSyCDKSQdglP_kfxPsZsDfqXxO0T193LJZfs'
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={zip_code}&key={key}'

    data = requests.get(url).json()

    longitude = data["results"][0]["geometry"]["location"]["lng"]
    latitude = data["results"][0]["geometry"]["location"]["lat"]
    address = data["results"][0]["formatted_address"]

    new_point = Point(zip_code=zip_code, longitude=longitude, latitude=latitude, address=address)

    db.session.add(new_point)
    db.session.commit()

    return render_template('result.html', zip_code=zip_code, longitude=longitude, latitude=latitude, address=address)


@app.route("/result-all")
def result_all():
    from models import Point
    points = Point.query.all()
    return render_template('result_all.html', points=points)


if __name__ == "__main__":
    app.run(debug=True)
