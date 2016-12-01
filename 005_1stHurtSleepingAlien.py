# import the time module
import time

alien = Actor('alien')

alien.topright = 0, 10

WIDTH = 500
HEIGHT = alien.height + 20

def draw():
    screen.clear()
    alien.draw()

def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0

# Uiui, we now move back to an unHurt alien. But is this really practical and is
# this how games are supposed to work?
def on_mouse_down(pos, button):
    if button == mouse.LEFT and alien.collidepoint(pos):
        sounds.eep.play()
        alien.image = 'alien_hurt'
        time.sleep(1)
        alien.image = 'alien'
    else:
        print("You missed me!")
