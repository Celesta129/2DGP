from pico2d import *

import random



open_canvas()

character = load_image('animation_sheet.png')
ground = load_image('KPU_GROUND.png')


frame = 0
t = 0
n = 0
points = [(random.randint(100,700),random.randint(50,550)) for n in range(10)]

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
    global t
    global points
    global n
    global direction

    if points[n][0] < points[n+1][0]:
        direction = 'Right'
    else:
        direction = 'Left'
    t += 0.01
    if t > 1:
        t = 0
        n = (n + 1) % len(points)

    characterX = ((-t ** 3 + 2 * t ** 2 - t) * points[n-1][0] + (3 * t ** 3 - 5 * t ** 2 + 2) * points[n][0] + (-3 * t ** 3 + 4 * t ** 2 + t) *
         points[n+1][0] + (t ** 3 - t ** 2) * points[n+2][0]) / 2
    characterY =  ((-t ** 3 + 2 * t ** 2 - t) * points[n-1][1] + (3 * t ** 3 - 5 * t ** 2 + 2) * points[n][1] + (-3 * t ** 3 + 4 * t ** 2 + t) *
         points[n+1][1] + (t ** 3 - t ** 2) * points[n+2][1]) / 2
    pass


while True:
    move_character()
    draw()

close_canvas()