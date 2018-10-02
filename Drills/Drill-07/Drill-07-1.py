from pico2d import *

import random




open_canvas()

character = load_image('animation_sheet.png')
ground = load_image('KPU_GROUND.png')


frame = 0
param = 0

points = [(random.randint(-350,350),random.randint(-250,250)) for n in range(20)]

characterX = points[0][0]
characterY = points[0][1]


def draw():
    global characterX, characterY
    clear_canvas()
    ground.draw(400,300)
    character.clip_draw(frame * 100,0,100,100, characterX, characterY)
    update_canvas()
    delay(0.01)
    get_events()
    pass


def move_character():
    global param


    param += 0.01
    pass


while True:
    move_character()
    draw()

close_canvas()