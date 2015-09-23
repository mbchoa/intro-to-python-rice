#http://www.codeskulptor.org/#user40_JrUi2op25Z_0.py

import simplegui
import random

# template for "Stopwatch: The Game"

# define global variables
width = 300
height = 200
time = 0
num_stops = 0;
num_stop_hit = 0;
timer_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes = t / 600
    seconds = t % 600 / 10
    tenth_second = t % 600 % 10
    if seconds < 10:
        seconds = '0' + str(seconds)
    else:
        seconds = str(seconds)
    return str(minutes) + ':' + seconds + '.' + str(tenth_second)
    
def score():
    return str(num_stops) + '/' + str(num_stop_hit)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()
    global timer_running
    timer_running = True
    
def stop_handler():
    global timer_running
    if timer_running:
        timer.stop()
        global num_stops
        num_stops += 1
        if time % 600 % 10 == 0:
            global num_stop_hit
            num_stop_hit += 1
        timer_running = False

def reset_handler():
    timer.stop()
    global time
    time = 0
    global num_stops
    num_stops = 0
    global num_stop_hit
    num_stop_hit = 0
    global timer_running
    timer_running = False

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1

# define draw handler
def draw_handler(canvas):
    if timer_running:
        color = "#%06x" % random.randint(0, 0xFFFFFF)
        canvas.draw_text(format(time), [width * 0.5, height * 0.5], 24, color)
    else:
        canvas.draw_text(format(time), [width * 0.5, height * 0.5], 24, 'White')
    canvas.draw_text(score(), [242, 48], 24, 'White')
    
# create frame
frame = simplegui.create_frame("Stop Watch", width, height)

# register event handlers
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, timer_handler)
start_btn = frame.add_button("Start", start_handler)
stop_btn = frame.add_button("Stop", stop_handler)
reset_btn = frame.add_button("Reset", reset_handler)

# start frame
frame.start()
