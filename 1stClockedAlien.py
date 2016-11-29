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

def on_mouse_down(pos, button):
    if button == mouse.LEFT and alien.collidepoint(pos):
        setAlienHurt()
    else:
        print("You missed me!")

# Nice, we have a clock now. Wait? Why do aliens need clocks?
# Remember our earlier bug?
def setAlienHurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(setAlienNormal, 1.0)

def setAlienNormal():
    alien.image = 'alien'
