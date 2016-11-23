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

# More fine-grained if, see how you can check for the LEFT button… try what
# happens if you use RIGHT, also, on-click we change the aliens' image to
# alien_hurt. But there is a bug, what is the Bug?
def on_mouse_down(pos, button):
    if button == mouse.LEFT and alien.collidepoint(pos):
        sounds.eep.play()
        alien.image = 'alien_hurt'
    else:
        print("You missed me!")
