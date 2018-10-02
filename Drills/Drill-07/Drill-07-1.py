from pico2d import *

import random
open_canvas()

character = load_image('animation_sheet.png')
frame = 0
ground = load_image('KPU_GROUND.png')

points = [(random.randint(-500,500),random.randint(-300,300)) for n in range(20)]

def draw():
    pass
def move_charactor():
    pass
while True:
    move_charactor()
    draw()

close_canvas()