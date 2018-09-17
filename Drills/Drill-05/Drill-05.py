from pico2d import *

open_canvas()
character = load_image('animation_sheet.png')

position = [(203, 535), (213, 243), (535, 470), (477, 203), (715, 136), (316, 225), (510, 92), (692, 518), (682, 336), (712, 349)]
frame = 0

def run_charactor():
    run_pos1()
    run_pos2()
    run_pos3()
    run_pos4()
    run_pos5()
    run_pos6()
    run_pos7()
    run_pos8()
    run_pos9()
    run_pos10()
    pass


def run_pos1():
    x = position[0][0]
    y = position[0][1]
    while x != position[1][0] and y != position[1][1]:
        clear_canvas()
        x = x + (position[1][0] - position[0][0]) * 0.1
        y = y + (position[1][1] - position[0][1]) * 0.01
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        delay(0.1)
    pass


def run_pos2():
    pass
def run_pos3():
    pass
def run_pos4():
    pass
def run_pos5():
    pass
def run_pos6():
    pass
def run_pos7():
    pass
def run_pos8():
    pass
def run_pos9():
    pass
def run_pos10():
    pass


while(True):

    run_charactor()

close_canvas()