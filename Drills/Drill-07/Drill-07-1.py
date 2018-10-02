from pico2d import *

import random




open_canvas()

character = load_image('animation_sheet.png')
ground = load_image('KPU_GROUND.png')


frame = 0
param = 0
n = 1
points = [(random.randint(100,700),random.randint(50,550)) for n in range(20)]

characterX = points[n-1][0]
characterY = points[n-1][1]

direction = 'Right'

def draw():
    global characterX, characterY
    global frame
    clear_canvas()
    ground.draw(400,300)
    if direction == 'Left':
        character.clip_draw(frame * 100,0,100,100, characterX, characterY)
    else:
        character.clip_draw(frame * 100, 100, 100, 100, characterX, characterY)
    update_canvas()
    delay(0.01)
    frame = (frame+1) % 8
    get_events()
    pass


def move_character():
    global characterX, characterY
    global param
    global points
    global n
    global direction

    if points[n-1][0] < points[n][0]:
        direction = 'Right'
    else:
        direction = 'Left'
    param += 0.01
    if param > 1:
        param = 0
        n = (n + 1) % len(points)

    characterX = points[n-1][0] * (1 - param) + points[n][0] * param
    characterY = points[n-1][1] * (1 - param) + points[n][1] * param
    pass


while True:
    move_character()
    draw()

close_canvas()