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

# Refactoring time! Remember functions? (def foo(): )
# To make the code more clean we create setAlienHurt()
def on_mouse_down(pos, button):
    if button == mouse.LEFT and alien.collidepoint(pos):
        setAlienHurt()
    else:
        print("You missed me!")

# Aw, nice. We never talked about the sounds yet. What does pgzero assume?
# On the Folder front? … And for images?
def setAlienHurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()

# This gets called to reset the alien to a normal state.
# But wait a minute. It isn't called anywhere yet?!!?
def setAlienNormal():
    alien.image = 'alien'
