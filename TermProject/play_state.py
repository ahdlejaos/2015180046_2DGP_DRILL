import pico2d
from pico2d import *
from boy_grass_object import *
import game_framework
import item_state
import title_state

boy = None
grass = None
running = None
def enter():
    global boy,grass, running
    boy = Boy()
    grass = Grass()
    running = True
def exit():
    global boy,grass
    del boy
    del grass

def update():
    boy.update()

def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_i:
                game_framework.push_state(item_state)
        #elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
        #    game_framework.change_state(title_state)
    delay(0.01)

def test_self():
    import play_state
    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.close_canvas()

def pause():
    pass

def resume():
    pass

if __name__ == '__main__':
    test_self()

open_canvas()

enter()

