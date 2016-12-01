alien = Actor('alien')

alien.topright = 0, 10

WIDTH = 500
HEIGHT = alien.height + 20

def draw():
    screen.clear()
    alien.draw()

# This is where you want to move things around, it gets called once (1) per frame
def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0

# SO now it knows when we click on it. But where do we click and why is the variable pos
# in the picture all of a sudden (without defining it?!?!?) print() anyone?
def on_mouse_down(pos):
    # Let us see where the mouse is
    print("Mouse position: {}".format(pos))
    if alien.collidepoint(pos):
        print("Eek!")
    else:
        print("You missed me!")
