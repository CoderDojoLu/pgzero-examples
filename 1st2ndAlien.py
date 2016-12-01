alien = Actor('alien')
coolAlien = Actor('cool_alien')

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

actors = [alien, coolAlien]
# some preliminary debug
for actor in actors:
    print("Actor in variable '{}' height: {}".format(namestr(actor, globals())[0], actor.height))
    print("Actor in variable '{}' width: {}".format(namestr(actor, globals())[0], actor.width))

# Play around with the aliens .pos parameter, what do you observe?
alien.pos = 100, 56

coolAlien.pos = 0, 600

# More magic, what happens if the screen is too small? Oh and what is the
# .height option? print() anyone?
WIDTH = 500
if alien.height > coolAlien.height:
    HEIGHT = alien.height + 20
else:
    HEIGHT = coolAlien.height + 20

# The draw function draws all elements once and should not be used for moving stuff across the screen
def draw():
    screen.clear()
    alien.draw()
    coolAlien.draw()
