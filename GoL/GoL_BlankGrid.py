WIDTH = 640
HEIGHT = 480
TITLE = 'Game of Life'
CELLSIZE = 10
assert WIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size"
assert HEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size"
CELLWIDTH = WIDTH / CELLSIZE # number of cells wide
CELLHEIGHT = HEIGHT / CELLSIZE # Number of cells high

# set up the colours
BLACK =    (0,  0,  0)
WHITE =    (255,255,255)
DARKGRAY = (40, 40, 40)

#Draws the grid lines
def draw():
    screen.fill(WHITE)
    for x in range(0, WIDTH, CELLSIZE): # draw vertical lines
        screen.draw.line((x,0),(x,HEIGHT), DARKGRAY)
    for y in range (0, HEIGHT, CELLSIZE): # draw horizontal lines
        screen.draw.line((0,y), (WIDTH, y), DARKGRAY)
