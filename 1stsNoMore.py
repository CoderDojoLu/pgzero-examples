# 1sts are fun but at a certain point we need to move on and just switch speeds.
# This time is now, in this example we will mix our rectangles with images and
# use a few loops to have more fun, for example if we want to generate a random
# forest, in code.

# remember we have a nice colors.py file, let's use it and just not think too
# much about redefining colors ourselves, read colors.py to know what is available
from colors import *

BOX1 = Rect((20,20), (100,100))
BOX2 = Rect((40,40), (200,200))

def draw():
    screen.draw.rect(BOX1, RED)
    screen.draw.rect(BOX2, BLUE)
    for i in range(42):
        BOX = Rect((20,20),(100+(3*i),100+(3*i)))
        screen.draw.rect(BOX, PURPLE)
