# mod3: 531.140s
# mod4: 581.388s 

import turtle
import pyautogui
from mytouchylib import *

# EDIT OPTIONS HERE
# SET TO TRUE TO DRAW IMAGE WITH TURTLE
drawturtle = False
# SET TO TRUE TO REPLAY EVENTS
replayactions = False
# Save the drawn image to postscript file
savepostscript = True
# Print actions to console
debugconsole = True
# Print actions to file
debugfile = False
# Select the touch events log file
touchfilename = "touchmod4.log"
# EDIT OPTIONS ^^^

scale = 4
scalex = scale
scaley = scale

def get_touches():
    t = []
    colr = ["black", "red", "green", "blue"]
    for n in range(4):
        touch = turtle.Turtle()
        touch.color(colr[n])
        touch.pensize(1)
        t.append(touch)
    return t

if drawturtle:
    w = turtle.Screen()
    # w.setup(width = 259, height = 173)
    w.setup(width = 1.0, height = 1.0)
    w.bgcolor("white")
    w.title(touchfilename)
    touches = get_touches()

resolution = pyautogui.size()
resabsx = resolution.width / 100.0
resabsy = resolution.height / 100.0

if debugfile:
    log = open("draw.log", "w")
    
f = open(touchfilename, "r")
for line in f.readlines():
    if "TOUCH_DOWN" in line:
        seat_slot = read_slots(line)
        coords = read_coords(line)
        if replayactions:
            if seat_slot == 0:
                pyautogui.moveTo(coords[0] * resabsx, coords[1] * resabsy)
                pyautogui.mouseDown()
                # pyautogui.mouseDown(coords[0] * resabsx, coords[1] * resabsy)
        if drawturtle:
            touches[seat_slot].goto([coords[0]*scalex, -coords[1]*scaley])
            touches[seat_slot].down()
        if debugfile:
            log.write("TOUCH_DOWN: {}\n".format(coords))
        if debugconsole:
            print(line)
    if "TOUCH_MOTION" in line:
        seat_slot = read_slots(line)
        coords = read_coords(line)
        if replayactions:
            if seat_slot == 0:
                pyautogui.moveTo(coords[0] * resabsx, coords[1] * resabsy)
        if drawturtle:
            touches[seat_slot].goto([coords[0]*scalex, -coords[1]*scaley])
        if debugfile:
            log.write("TOUCH_MOTION: {}\n".format(coords))
        if debugconsole:
            print(line)
    if "TOUCH_UP" in line:
        seat_slot = read_slots(line)
        if replayactions:
            if seat_slot == 0:
                pyautogui.mouseUp()
        if drawturtle:
            touches[seat_slot].up()
        if debugfile:
            log.write("TOUCH_UP: {}\n".format(coords))
        if debugconsole:
            print(line)


if drawturtle and savepostscript:
    n = 0
    for t in touches:
        # let's force fullscreen otherwise the output is cut...
        w.setup(width = 1.0, height = 1.0)
        w.getcanvas().winfo_toplevel().overrideredirect(1)
        t.getscreen().getcanvas().postscript(file='touch{}.ps'.format(n), height=resolution.height, width=resolution.width)
        w.getcanvas().winfo_toplevel().overrideredirect(0)
        n += 1
        break

print("DONE")

if drawturtle:
    w.mainloop()