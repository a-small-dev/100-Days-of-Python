up_pressed = False
down_pressed = False
w_pressed = False
s_pressed = False

def up_press():
    global up_pressed
    up_pressed = True

def up_release():
    global up_pressed
    up_pressed = False

def down_press():
    global down_pressed
    down_pressed = True

def down_release():
    global down_pressed
    down_pressed = False

def w_press():
    global w_pressed
    w_pressed = True

def w_release():
    global w_pressed
    w_pressed = False

def s_press():
    global s_pressed
    s_pressed = True

def s_release():
    global s_pressed
    s_pressed = False