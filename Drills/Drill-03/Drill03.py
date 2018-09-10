from pico2d import *
import math

open_canvas()
character = load_image('character.png')
grass = load_image('grass.png')


x = 400
y = 90

angle = -90
dir = 0
# 0 = right, 1 = up, 2 =left, 3 = down

switch = True
# F: rect/ T: circle
# circle로 초기화 한뒤 시작하자마자 rect로 바꿔준다.
while(True):
    clear_canvas_now()    
    character.draw_now(x,y)
    grass.draw_now(400,30)
    if(x == 400 and y == 90):
        switch = not switch
   
    if(switch == True):
        if dir == 0:
            x = x+1
            if x == 800:
                dir = 1
        elif dir == 1:
            y = y+1
            if y == 600:
                dir = 2
        elif dir == 2:
            x = x-1
            if x == 0:
                dir = 3
        elif dir == 3:
            y = y-1
            if y == 90:
                dir = 0
    elif switch == False:
        x =  math.cos(angle) * 210 + 400
        y = math.sin(angle) * 210 + 300
        angle = angle + 3
        if angle == 360:
            angle = 0
            x = 400
            y = 90
        
