from pico2d import *
from math import*

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=50
y=90

def draw():
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)



while(1):
    
    
    while(x<750):
        draw()
        x+=5
        delay(0.01)
        
    while(y<550):
        draw()
        y+=5
        delay(0.01)
        
    while(x>50):
        draw()
        x-=5
        delay(0.01)
            
    while(y>90):
        draw()
        y-=5
        delay(0.01)
                
    
close_canvas()        



        
                        
        
    




    
