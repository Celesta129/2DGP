from pico2d import *

x = 0
dir = 90
# 90 = right, 0 = left
frame = 0
open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

while(True):
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame*100,dir,100,100,x,90)
    update_canvas()
    frame = (frame +1 ) % 8
    if(dir == 90):
        x +=5
    else:
        x -= 5

    if( x == 800):
        dir = 0
    elif x == 0:
        dir = 90
    delay(0.05)
    get_events()

close_canvas()
