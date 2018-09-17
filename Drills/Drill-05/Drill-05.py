from pico2d import *
open_canvas()
character = load_image("animation_sheet.png")
grass = load_image("grass.png")

Arr_position = [(203, 535), (132, 243), (535, 470), (477, 203), (715, 136),
            (316, 225), (510, 92), (692, 518), (682, 336), (712, 349)]

frame = 0
posNumber = 0
direction = "Right"
x = Arr_position[posNumber][0]
y = Arr_position[posNumber][1]


def move_character():
    pass


def draw():
    global frame
    global x
    global y
    global posNumber

    clear_canvas()
    grass.draw(400, 30)

    if direction == "Left":
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)

    update_canvas()
    frame = (frame + 1) % 8

    pass


while True:
    move_character()
    draw()

    delay(0.05)
    get_events()
    pass

close_canvas()