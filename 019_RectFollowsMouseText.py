# remember we have a nice colors.py file, let's use it and just not think too
# much about redefining colors ourselves, read colors.py to know what is available
# please use python3 -m pgzero mySource.py to run when import local modules
try:
    from colors import *
except ImportError:
    raise ImportError('please use the python interpreter directly, pgzrun has issues with local module imports: python3 -m pgzero 019_RectFollowsMouseText.py')

# Define our 800x600 screen
WIDTH = 800
HEIGHT = 600

# This will literally put a rectangle with certain properties into the variable BOX
BOX1 = Rect((0,0), (0,0))
BOX2 = Rect((20,20), (100,100))

# As we know, we need the draw function to put stuff on the screen
def draw():
    # What if we do not clear the screen?
    screen.clear()

    # Needs to be define before we use growMin and growMax
    mouseFont = fontNormalized(mousePos[1])

    # We simply draw, to the screen, the variable BOX with the color in RED
    screen.draw.rect(BOX1, RED)
    screen.draw.rect(BOX2, BLUE)

    # 2 Lines to show when we stop growing our font
    screen.draw.line((0,growMin), (WIDTH, growMin),(GREEN),3)
    screen.draw.line((0,growMax), (WIDTH, growMax),(GREEN10),3)

    # Draw some text on the screen to give an idea where our mouse is at
    screen.draw.text(
                        'mouseX: {0} mouseY: {1}'.format(mousePos[0], mousePos[1]),
                        center=((WIDTH/2), 20),
                        sysfontname='arial',
                        fontsize=48,
                        color=YELLOW,
                    )

    screen.draw.text(
                        '{}'.format(mousePos),
                        center=mousePos,
                        sysfontname='arial',
                        fontsize=mouseFont,
                        color=PINK,
        )

def on_mouse_move(pos):
    global mousePos
    x, y = pos
    BOX1.size = (x, y)
    BOX2.center = (x, y)
    mousePos = pos

def fontNormalized(posY):
    global growMin
    global growMax
    growMin = 40
    growMax = 100

    if posY < growMin:
        return growMin
    elif posY > growMax:
        return growMax
    else:
        return posY
