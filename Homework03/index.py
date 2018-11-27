# Import gui
import simplegui

# Define global vars
counter = 0
total_stops = 0
successful_stops = 0
run = True


# Define counter increment
def tick():
    global counter
    counter += 1


# Define buttons
def start():
    global run
    run = True
    timer.start()


def reset():
    global counter, total_stops, successful_stops
    counter = 0
    total_stops = 0
    successful_stops = 0
    timer.stop()


def stop():
    global run, total_stops, successful_stops
    if run is True:
        if int(str(counter)[-1]) == 0 and counter != 0:
            successful_stops += 1
            total_stops += 1
        elif counter != 0:
            total_stops += 1
        run = False
    timer.stop()


# Define deciseconds to string function
def format(t):
    deciseconds = (t) % 10  # D in A:BC.D
    seconds2 = int(t / 10) % 10  # C in A:BC.D
    seconds1 = int(t / 100) % 6  # B in A:BC.D
    minutes = int(t // 600)  # A in A:BC.D
    string = str(minutes) + ":" + str(seconds1) + str(seconds2) + "." + str(deciseconds)
    return string


# Define draw handler
def draw(canvas):
    text = format(counter)
    canvas.draw_text(text, (140, 180), 50, "yellow")
    canvas.draw_text(str(successful_stops) + '/' + str(total_stops), (330, 40), 35, "yellow")

# Create a frame
frame = simplegui.create_frame("StopGame", 400, 400)

# Register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)
frame.add_button("Start", start, 150)
frame.add_button("Stop", stop, 150)
frame.add_button("Reset", reset, 150)

# Start frame
frame.start()

