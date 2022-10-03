from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
# def handle_events():
#     global running
#     global x,y
#     events = get_events()
#     for event in events:
#         if event.type == SDL_QUIT:
#             running = False
#         elif event.type == SDL_MOUSEMOTION:
#             x,y = event.x ,TUK_HEIGHT - 1 - event.y
#         elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
#             running = False
def handle_events():
    global running
    global dirX
    global dirY
    global frameMove
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                frameMove = 1
                dirX += 1
            elif event.key == SDLK_LEFT:
                frameMove = 2
                dirX -= 1
            elif event.key == SDLK_UP:
                dirY += 1
            elif event.key == SDLK_DOWN:
                dirY -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                frameMove = 3
                dirX -= 1
            elif event.key == SDLK_LEFT:
                frameMove = 2
                dirX += 1
            elif event.key == SDLK_UP:
                dirY -= 1
            elif event.key == SDLK_DOWN:
                dirY += 1


    pass

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dirX = 0
dirY = 0
block = 5
frameMove = 3
hide_cursor()

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * frameMove , 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    x += dirX * 5
    if x > TUK_WIDTH :
        x = TUK_WIDTH - block
    y += dirY * 5
    if y > TUK_HEIGHT:
        y = TUK_HEIGHT - block
    handle_events()

close_canvas()




