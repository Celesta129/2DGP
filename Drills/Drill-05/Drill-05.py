from pico2d import *
open_canvas()
character = load_image("animation_sheet.png")
grass = load_image("grass.png")

Arr_position = [(203.0, 535.0), (132.0, 243.0), (535.0, 470.0), (477.0, 203.0), (715.0, 136.0),
            (316.0, 225.0), (510.0, 92.0), (692.0, 518.0), (682.0, 336.0), (712.0, 349.0)]

frame = 0
PosIndex = {"Current" : 0, "Next" : 1}
direction = "Right"
x = Arr_position[0][0]
y = Arr_position[0][1]


def move_character():
    pass

def draw():
    pass

while True:
    move_character()
    draw()

    delay(0.05)
    get_events()
    pass

close_canvas()