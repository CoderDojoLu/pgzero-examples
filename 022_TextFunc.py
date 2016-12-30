#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import pgzero wrapper workaround to easily call it from the CLI
try:
    from runpgzero import *
except ImportError:
    raise ImportError('Is runpgzer.py in your current working directory?')
# remember we have a nice colors.py file, let's use it and just not think too
# much about redefining colors ourselves, read colors.py to know what is available
# please use python3 -m pgzero mySource.py to run when import local modules
try:
    from colors import *
except ImportError:
    raise ImportError('Is colors.py in your current working directory?')

''' Declarations '''

# Define our 800x600 screen
WIDTH = 800
HEIGHT = 600


''' Game Loop '''

# As we know, we need the draw function to put stuff on the screen
def draw():
    # What if we do not clear the screen?
    screen.clear()

    # Needs to be define before we use growMin and growMax
    mouseFont = fontNormalized(mousePos[1])

    # Draw some text on the screen to give an idea where our mouse is at
    screen.draw.text(
                        'mouseX: {0} mouseY: {1}'.format(mousePos[0], mousePos[1]),
                        center=((WIDTH/2), 20),
                        fontsize=48,
                        color=YELLOW,
                    )

    screen.draw.text(
                        '{}'.format(mousePos),
                        center=mousePos,
                        fontsize=mouseFont,
                        color=PINK,
        )

def on_mouse_move(pos):
    global mousePos
    x, y = pos
    BOX1.size = (x, y)
    BOX2.center = (x, y)
    mousePos = pos



# Run the above code
run_pgzero()
