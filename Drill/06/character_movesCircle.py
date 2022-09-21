from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    centerX = 400
    centerY = 300
    r = 200   
    
    for deg in range(0,360,5):
        x = centerX + r * math.cos(deg / 360 * 2 * math.pi)
        y = centerY + r * math.sin(deg / 360 * 2 * math.pi)
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.1)


def draw():
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    


while(1):
    run_circle()
    break
    
    


    
 
                
    
    



        
                        
        
    




    
