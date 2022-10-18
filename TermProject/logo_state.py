import game_framework
import title_state
from pico2d import *

running  = True
image = None
logo_time = 0.0

# fill here

def enter():
    global image
    image = load_image('tuk_credit.png')
    pass

def exit():
    global image
    del image
    pass

def update():
    global logo_time
    #global running
    if logo_time > 1.0:
        logo_time = 0
        game_framework.change_state(title_state)
        #game_framework.quit()
        #running = False
    delay(0.05)
    logo_time += 0.01
def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
def handle_events():
    events = get_events()





