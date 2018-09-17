from pico2d import *
open_canvas()
character = load_image("animation_sheet.png")
grass = load_image("grass.png")

position = [(203, 535), (132, 243), (535, 470), (477, 203), (715, 136),
            (316, 225), (510, 92), (692, 518), (682, 336), (712, 349)]


def move_character():
    pass


while True:
    move_character()
    pass

close_canvas()