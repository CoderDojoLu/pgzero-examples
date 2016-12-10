RED = 150, 0, 0
GREEN = 0, 128, 0

bg = RED

def draw():
    screen.fill(bg)

def on_mouse_down():
    global bg
    bg = GREEN

def on_mouse_up():
    global bg
    bg = RED
