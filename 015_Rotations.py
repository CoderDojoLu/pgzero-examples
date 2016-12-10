import time

from pygame.transform import flip, rotate

angle = 0
rotated = rotate(images.spinner, angle)

rotor = Actor('spinner')

WIDTH = rotor.width * 2
HEIGHT = rotor.height * 2

def draw():
    screen.clear()
    screen.blit(rotated, (0,0))
    print("draw() type(rotated) {}".format(type(rotated)))

def on_mouse_down(pos, button):
    global rotated
    global angle
    rotated = rotate(images.spinner, angle)
    angle += 1
