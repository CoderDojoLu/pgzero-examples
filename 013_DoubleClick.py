from time import time
# We used da emojis again, because we can :) oh, sorry: 😃
from emoji import emojize

# Panic buttons are panicky: https://en.wikipedia.org/wiki/Panic_button
panic = Actor('640px-hazard_warning_flasher_button')

# We plainly set our screen size to the size of our image
WIDTH = panic.width
HEIGHT = panic.height

# This is a simple and stupid double click implementation
# And we will define some global variables that will be visible in all our
# functions that handle mouse events (or any other functions, like draw())
lastClick = currentClick = 0

# Here we define the duration of the double click
double_click_duration = 0.5

def draw():
    panic.draw()

def on_mouse_down(pos, button):
    global lastClick
    global double_click_duration
    now = time()
    print("You clicked the", button.name.lower(), "mouse button at", pos)
    if now - lastClick <= double_click_duration:
        print(emojize(':mouse: double click', use_aliases=True))
    lastClick = time()
