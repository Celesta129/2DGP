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
    global x
    global y
    global PosIndex

    nextIndex = PosIndex["Next"]
    currentIndex = PosIndex["Current"]

    x = x + (Arr_position[nextIndex][0] - Arr_position[currentIndex][0]) * 0.05
    y = y + (Arr_position[nextIndex][1] - Arr_position[currentIndex][1]) * 0.05

    xCheck = Arr_position[nextIndex][0]*0.95 < x <= Arr_position[nextIndex][0] * 1.05
    yCheck = Arr_position[nextIndex][1]*0.95 < y <= Arr_position[nextIndex][1] * 1.05

    Change_Direction()

    if xCheck and yCheck:
        PosIndex["Next"] = PosIndex["Next"] + 1
        PosIndex["Current"] = PosIndex["Current"] +1
        if PosIndex["Next"] == 10:
            PosIndex["Next"] = 0

        if PosIndex["Current"] == 10:
            PosIndex["Current"] = 0
        pass

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

    pass

def Change_Direction():
    pass

while True:
    move_character()
    draw()

    delay(0.05)
    get_events()
    pass

close_canvas()