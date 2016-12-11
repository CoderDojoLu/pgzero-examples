import random

#Number of frames per second, not used at the moment
FPS = 10

###Sets size of grid
WIDTH = 640
HEIGHT = 480
TITLE = 'Game of Life'
CELLSIZE = 10

#Check to see if the width and height are multiples of the cell size.
assert WIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size"
assert HEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size"

#Determine number of cells in horizontal and vertical plane
CELLWIDTH = WIDTH / CELLSIZE # number of cells wide
CELLHEIGHT = HEIGHT / CELLSIZE # Number of cells high

# set up the colours
BLACK =    (0,  0,  0)
WHITE =    (255,255,255)
DARKGRAY = (40, 40, 40)
GREEN =    (0,255,0)

#Draws the grid lines
def drawGrid():
    for x in range(0, WIDTH, CELLSIZE): # draw vertical lines
        screen.draw.line((x,0),(x,HEIGHT), DARKGRAY)
    for y in range (0, HEIGHT, CELLSIZE): # draw horizontal lines
        screen.draw.line((0,y), (WIDTH, y), DARKGRAY)

#Creates an dictionary of all the cells
#Sets all cells as dead (0)
def blankGrid():
    gridDict = {}
    #creates dictionary for all cells
    for y in range (int(CELLHEIGHT)):
        for x in range (int(CELLWIDTH)):
            gridDict[x,y] = 0 #Sets cells as dead
    return gridDict

#Assigns a 0 or a 1 to all cells
def startingGridRandom(lifeDict):
    for item in lifeDict:
        lifeDict[item] = random.randint(0,1)
    return lifeDict

lifeDict = blankGrid() # creates library and Populates to match blank grid
lifeDict = startingGridRandom(lifeDict) # Assign random life

#Colours the cells green for life and white for no life
def colourGrid(item, lifeDict):
    x = item[0]
    y = item[1]
    y = y * CELLSIZE # translates array into grid size
    x = x * CELLSIZE # translates array into grid size
    if lifeDict[item] == 0:
        screen.draw.filled_rect(Rect((x, y), (CELLSIZE, CELLSIZE)), WHITE)
    if lifeDict[item] == 1:
        screen.draw.filled_rect(Rect((x, y), (CELLSIZE, CELLSIZE)), GREEN)
    return None

#Determines how many alive neighbours there are around each cell
def getNeighbours(item,lifeDict):
    neighbours = 0
    for x in range (-1,2):
        for y in range (-1,2):
            checkCell = (item[0]+x,item[1]+y)
            if checkCell[0] < CELLWIDTH  and checkCell[0] >=0:
                if checkCell [1] < CELLHEIGHT and checkCell[1]>= 0:
                    if lifeDict[checkCell] == 1:
                        if x == 0 and y == 0: # negate the central cell
                            neighbours += 0
                        else:
                            neighbours += 1
    return neighbours

#determines the next generation by running a 'tick'
def tick(lifeDict):
    newTick = {}
    for item in lifeDict:
        #get number of neighbours for that item
        numberNeighbours = getNeighbours(item, lifeDict)
        if lifeDict[item] == 1: # For those cells already alive
            if numberNeighbours < 2: # kill under-population
                newTick[item] = 0
            elif numberNeighbours > 3: #kill over-population
                newTick[item] = 0
            else:
                newTick[item] = 1 # keep status quo (life)
        elif lifeDict[item] == 0:
            if numberNeighbours == 3: # cell reproduces
                newTick[item] = 1
            else:
                newTick[item] = 0 # keep status quo (death)
    return newTick

def draw():
    # This does not work at the moment
    screen.fill(WHITE)

    #Colours the live cells, blanks the dead
    for item in lifeDict:
        colourGrid(item, lifeDict)
    drawGrid()

def update():
    global lifeDict
    #runs a tick
    lifeDict = tick(lifeDict)

    #Colours the live cells, blanks the dead
    for item in lifeDict:
        colourGrid(item, lifeDict)
    drawGrid()
