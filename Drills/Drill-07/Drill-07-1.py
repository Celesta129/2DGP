from pico2d import *

import random

character = load_image('animation_sheet.png')
ground = load_image('KPU_GROUND.png')

points = [(random.randint(-500,500),random.randint(-300,300)) for n in range(20)]
open_canvas()

close_canvas()