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
    move_Horizon()
    delay(0.5)
    move_Vertical()

    pass

def move_Horizon():
    draw()
    pass

def move_Vertical():
    draw()
    pass

def draw():
    global frame
    global x
    global y

    clear_canvas()
    grass.draw(400, 30)

    if direction == "Left":
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)

    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    pass


def Change_Direction(CurrentPos,NextPos):
    global direction
    if(CurrentPos > NextPos):
        direction = "Left"
    else:
        direction = "Right"
    pass


while True:
    move_character()
    get_events()
    pass

close_canvas()