from pico2d import *
from FrameWork import MainFrameWork
from FrameWork.State import State_Stage
from FrameWork import Game_World

name = "State_Pause"
image1 = None
image2 = None
cur_button = 0

RETURN,RESTART,EXIT,BUTTON_END = range(4)
def enter():
    global image1, image2
    if image1 == None:
        image1 = load_image("Pause1.png")
    if image2 == None:
        image2 = load_image("Pause2.png")

    global cur_button
    cur_button = 0
    pass
def exit():
    global image1, image2
    del image1, image2
    image1, image2 = None,None
    pass

def pause():
    pass
def resume():
    pass

def handle_events():
    global cur_button
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            MainFrameWork.quit()
        elif event.type == SDL_KEYDOWN and (event.key == SDLK_ESCAPE or event.key == SDLK_x):
            MainFrameWork.pop_state()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            cur_button = (cur_button - 1) % BUTTON_END
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            cur_button = (cur_button + 1) % BUTTON_END

        elif event.type == SDL_KEYDOWN and event.key == SDLK_z:
            if cur_button == 0:
                MainFrameWork.pop_state()
            elif cur_button == 1:
                MainFrameWork.pop_state()
                MainFrameWork.pop_state()
                MainFrameWork.push_state(State_Stage)
                pass
            elif cur_button == 2:
                MainFrameWork.quit()

    pass

def draw():
    global cur_button
    x,y = 250, 300
    clear_canvas()
    MainFrameWork.stack[-2].draw()
    image1.clip_draw(0,0,128,128,x,y)
    image2.clip_draw(cur_button * 128,0,128,128,x,y - 50)
    update_canvas()
    pass

def update():
    pass

