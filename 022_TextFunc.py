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

    # Use our drawText() function
    drawText()

def on_mouse_move(pos):
    global mousePos
    x, y = pos
    mousePos = pos

def drawText(msg='Please set a message', fontSize=24, color=WHITE, center=(WIDTH/2, HEIGHT/2)):
    # Draw some text on the screen to give an idea where our mouse is at
    screen.draw.text(
                        str(msg),
                        center=center,
                        fontsize=fontSize,
                        color=color,
                    )


# Run the above code
run_pgzero()
