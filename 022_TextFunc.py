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
    # Our function can be called with no arguments but will show a place holder
    drawText()
    # The next example draws a custom text, custom font size, custom color, but by default centered x=-20, y=+20 in the middle of the screen
    drawText('The text above text is the draw text function called without any parameters', 26, RED4, ((WIDTH/2)-20, (HEIGHT/2)+20))
    # Quick example on putting text at the 0,0 (top left) location of the game screen
    drawText('Here we draw text at 0,0 - BUT, center needs to be set to None', center=None, pos=(0,0))
    # Quick example on putting text at an arbitrary x/y location
    drawText('We are now drawing text at: x=60, y=120', center=None, pos=(60,120))
    # You can draw text in a loop, of course :)
    fontSize=24
    repeat=5
    for space in range(repeat):
        drawText('This text will repeat {} time(s) and position the text one under another, in a loop.'.format(repeat), center=None, pos=(0, (HEIGHT/2)+40+fontSize*space))
    # Color from a list example
    myColors = [RED, GREEN, BLUE, CYAN, MAGENTA, PURPLE]
    repeat = len(myColors)
    for space in range(repeat):
        drawText('This text will repeat {} time(s) and position the text one under another, in a loop, with colors from a list.'.format(repeat), center=None, pos=(0, (HEIGHT/2)+40+120+fontSize*space), color=myColors[space])

def on_mouse_move(pos):
    global mousePos
    x, y = pos
    mousePos = pos

def drawText(msg='Please set a message', fontSize=24, color=WHITE, center=(WIDTH/2, HEIGHT/2), pos=(0,0)):
    # Draw some text on the screen to give an idea where our mouse is at
    screen.draw.text(
                        str(msg),
                        center=center,
                        pos=pos,
                        fontsize=fontSize,
                        color=color,
                    )


# Run the above code
run_pgzero()
