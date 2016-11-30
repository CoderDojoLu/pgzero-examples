RED = 200, 0, 0

# When assigning a variable that is a tuple you can omit, or not, the
# parenthisis
BLUE = (0, 0, 200)

# Obviously we need 2 distinct variables, one for each element
BOX1 = Rect((20,20), (100,100))
BOX2 = Rect((40,40), (200,200))

def draw():
    # Finally we put both on the screen
    screen.draw.rect(BOX1, RED)
    screen.draw.rect(BOX2, BLUE)
