from pico2d import *
from FrameWork import MainFrameWork

name = "State_Stage"

image_Main_BG = None
image_Background = None
Background_Scroll_y = 0

player = None
def enter():
    global image_Main_BG
    global player
    if(player == None):
        pass
    if image_Main_BG == None:
        image_Main_BG = load_image("MainBackGround.png")


def exit():
    global image_Main_BG
    del(image_Main_BG)



def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            MainFrameWork.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            MainFrameWork.quit()
    pass


def update():
    pass


def draw():
    global image_Main_BG
    clear_canvas()

    image_Main_BG.clip_draw(0,0,121,159,400,300,800,600)

    update_canvas()
    pass