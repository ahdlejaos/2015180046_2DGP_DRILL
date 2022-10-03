from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('mario-sprite-sheet-png.png')

# 여기를 채우세요.
x = 0
frame = 0
while ( x < 800):
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame * 10, 0, 200, 200, x, 90)
    update_canvas()
    frame = (frame + 1) % 8
    x += 5
    delay(0.05)
    get_events()

close_canvas()

