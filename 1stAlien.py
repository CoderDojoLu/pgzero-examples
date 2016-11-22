# This seems like magic!?!!!! But why?
alien = Actor('alien')

# Play around with the aliens .pos parameter, what do you observe?
alien.pos = 100, 56

# More magic, what happens if the screen is too small? Oh and what is the
# .height option? print() anyone?
WIDTH = 500
HEIGHT = alien.height + 20

# The draw function draws all elements once and should not be used for moving stuff across the screen
def draw():
    screen.clear()
    alien.draw()
