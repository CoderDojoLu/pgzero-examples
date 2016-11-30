#!/usr/bin/env python3
import sys, random, pygame, time, os
from pygame.locals import *

FPS = 10
CELLSIZE=10
WIDTH=640
HEIGHT=480
FULLSCREEN=True
pygame.init()
global screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
flags = screen.get_flags()
bits = screen.get_bitsize()
w,h = screen.get_width(),screen.get_height()
screen = pygame.display.set_mode((w,h),flags^FULLSCREEN,bits)

assert w % CELLSIZE == 0, "WIDTH must be a multiple of CELLSIZE"
assert h % CELLSIZE == 0, "HEIGHT must be a multiple of CELLSIZE"
CELLWIDTH = w / CELLSIZE
CELLHEIGHT = h / CELLSIZE
x = 100
y = 0
#os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
os.environ['SDL_VIDEO_CENTERED'] = '1'

# env: SDL_WINDOW_FULLSCREEN - 

BLACK = (0,0,0)
WHITE = (255,255,255)
DARKGRAY = (40,40,40)
GREEN = (0, 255, 0)

def toggle_fullscreen():
    screen = pygame.display.get_surface()
    tmp = screen.convert()
    caption = pygame.display.get_caption()
    cursor = pygame.mouse.get_cursor()  # Duoas 16-04-2007

    w,h = screen.get_width(),screen.get_height()

    pygame.display.quit()
    pygame.display.init()

    screen = pygame.display.set_mode((w,h),flags^FULLSCREEN,bits)
    screen.blit(tmp,(0,0))
    pygame.display.set_caption(*caption)

    pygame.key.set_mods(0) #HACK: work-a-round for a SDL bug??

    pygame.mouse.set_cursor( *cursor )  # Duoas 16-04-2007

    return screen

def drawGrid():
    for x in range(0, WIDTH, CELLSIZE):
        pygame.draw.line(screen, DARKGRAY, (x,0), (x,HEIGHT))

    for y in range(0, HEIGHT, CELLSIZE):
        pygame.draw.line(screen, DARKGRAY, (0,y), (WIDTH, y))

def blankGrid():
    gridDict = {}
    for y in range(int(CELLHEIGHT)):
        for x in range(int(CELLWIDTH)):
            gridDict[x,y] = 0
    return gridDict

def colourGrid(item, lifeDict):
    x = item[0]
    y = item[1]
    y = y * CELLSIZE
    x = x * CELLSIZE
    if lifeDict[item] == 0:
        pygame.draw.rect(screen, WHITE, (x,y, CELLSIZE, CELLSIZE))
    if lifeDict[item] == 1:
        pygame.draw.rect(screen, GREEN, (x,y, CELLSIZE, CELLSIZE))
    return None

def getNeighbours(item,lifeDict):
    neighbours = 0
    for x in range(-1,2):
        for y in range(-1,2):
            checkCell = (item[0]+x, item[1]+y)
            if checkCell[0] < CELLWIDTH and checkCell[0] >= 0:
                if checkCell[1] < CELLHEIGHT and checkCell[1] >= 0:
                    if lifeDict[checkCell] == 1:
                        if x == 0 and y == 0:
                            neighbours += 0
                        else:
                            neighbours += 1
    return neighbours

def tick(lifeDict):
    newTick = {}
    for item in lifeDict:
        numberNeighbours = getNeighbours(item, lifeDict)
        if lifeDict[item] == 1:
            if numberNeighbours < 2:
                newTick[item] = 0
            elif numberNeighbours > 3:
                newTick[item] = 0
            else:
                newTick[item] = 1
        elif lifeDict[item] == 0:
            if numberNeighbours == 3:
                newTick[item] = 1
            else:
                newTick[item] = 0
    return newTick

def startingGridRandom(lifeDict):
    for item in lifeDict:
        lifeDict[item] = random.randint(0,1)
    return lifeDict

def main():
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Game of Life')
    screen.fill(WHITE)
    lifeDict = blankGrid()
    lifeDict = startingGridRandom(lifeDict)
    for item in lifeDict:
        colourGrid(item, lifeDict)

    drawGrid()
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type is KEYDOWN and event.key == K_ESCAPE: _quit = True
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if (event.type is KEYDOWN and event.key == K_RETURN
                    and (event.mod&(KMOD_LALT|KMOD_RALT)) != 0):
                toggle_fullscreen()

        lifeDict = tick(lifeDict)
        for item in lifeDict:
            colourGrid(item, lifeDict)

        drawGrid()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()