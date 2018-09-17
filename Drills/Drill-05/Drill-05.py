from pico2d import *
open_canvas()
character = load_image("animation_sheet.png")
grass = load_image("grass.png")

Arr_position = [(203, 535), (132, 243), (535, 470), (477, 203), (715, 136),
            (316, 225), (510, 92), (692, 518), (682, 336), (712, 349)]

frame = 0
PosIndex = {"Current" : 0, "Next" : 1}
direction = "Right"
x = Arr_position[0][0]
y = Arr_position[0][1]


def move_character():
    currentX = Arr_position[PosIndex["Current"]]
    nextX = Arr_position[PosIndex["Next"]]

    Change_Direction(currentX,nextX)
    move_Horizon()
    delay(0.5)
    move_Vertical()
    change_Index()

    pass
def change_Index():
    global PosIndex

    PosIndex["Current"] = PosIndex["Next"]
    PosIndex["Next"] = PosIndex["Next"] + 1
    if PosIndex["Next"] == 10:
        PosIndex["Next"] = 0
    pass
def move_Horizon():
    global x
    global PosIndex
    global Arr_position

    currentX = Arr_position[PosIndex["Current"]][0]
    nextX = Arr_position[PosIndex["Next"]][0]

    while x != nextX:
        if currentX > nextX:
            x = x - 1
        else:
            x = x + 1
        draw()
    pass

def move_Vertical():
    global y
    global PosIndex
    global Arr_position

    currentY = Arr_position[PosIndex["Current"]][1]
    nextY = Arr_position[PosIndex["Next"]][1]

    while y != nextY:
        if currentY > nextY:
            y = y - 1
        else:
            y = y + 1
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
    delay(0.01)
    get_events()
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

    pass

close_canvas()