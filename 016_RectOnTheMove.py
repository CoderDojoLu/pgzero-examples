WIDTH = 800
HEIGHT = 600

# The following will assign a tuple to the variable RED
RED = 200, 0, 0

# This will literally put a rectangle with certain properties into the variable BOX
BOX = Rect((20,20), (100,100))

# As we know, we need the draw function to put stuff on the screen
def draw():
    # What if we do not clear the screen?
    ## screen.clear()
    # We simply draw, to the screen, the variable BOX with the color in RED
    screen.draw.rect(BOX, RED)

def on_mouse_down(pos):
    x, y = pos
    BOX.center = (x, y)
