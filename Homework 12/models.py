from app import db


class Point(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    zip_code = db.Column(db.Integer)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    address = db.Column(db.String(128), index=True)

    def __init__(self, zip_code, longitude, latitude, address):
        self.zip_code = zip_code
        self.longitude = longitude
        self.latitude = latitude
        self.address = address
