# This seems like magic!?!!!! But why?
alien = Actor('alien')

# Play around with the aliens .pos parameter, what do you observe?
alien.topright = 0, 10

# More magic, what happens if the screen is too small? Oh and what is the
# .height option? print() anyone?
WIDTH = 500
HEIGHT = alien.height + 20

def draw():
    screen.clear()
    alien.draw()

# Yes, this function is still commented out, once having played around with .pos
# comment this in again and see what happens… but how?
#def update():
#    alien.left += 2
#    if alien.left > WIDTH:
#        alien.right = 0
