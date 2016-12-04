from time import time

# 3 different clicker backgrounds
click1 = Actor('click1')
click2 = Actor('click2')
click3 = Actor('click3')

WIDTH = click1.width
HEIGHT = click1.height

lastClick = currentClick = 0

double_click_duration = 0.5

# Set currently visible images to false
clicked1 = clicked2 = clicked3 = False

def draw():
    print(clicked2)
    if clicked2:
        print("Drawing clicked2")
        click2.draw()
    else:
        print("Drawing clicked1")
        click1.draw()

def on_mouse_down(pos, button):
    global lastClick
    global clicked2
    global double_click_duration
    now = time()
    print("You clicked the", button.name.lower(), "mouse button at", pos)
    if now - lastClick <= double_click_duration:
        print('double click')
        clicked2 = True
    lastClick = time()
    print(clicked2)
