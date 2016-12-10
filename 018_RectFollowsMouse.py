# remember we have a nice colors.py file, let's use it and just not think too
# much about redefining colors ourselves, read colors.py to know what is available
# please use python3 -m pgzero mySource.py to run when import local modules
try:
    from colors import *
except ImportError:
    raise ImportError('please use the python interpreter directly, pgzrun has issues with local module imports: python3 -m pgzero 1stText.py')

WIDTH = 800
HEIGHT = 600

# The following will assign a tuple to the variable RED
RED = 200, 0, 0

# This will literally put a rectangle with certain properties into the variable BOX
BOX1 = Rect((0,0), (0,0))
BOX2 = Rect((20,20), (100,100))

# As we know, we need the draw function to put stuff on the screen
def draw():
    # What if we do not clear the screen?
    screen.clear()
    # We simply draw, to the screen, the variable BOX with the color in RED
    screen.draw.rect(BOX1, RED)
    screen.draw.rect(BOX2, BLUE)

def on_mouse_move(pos):
    x, y = pos
    BOX1.size = (x, y)
    BOX2.center = (x, y)

