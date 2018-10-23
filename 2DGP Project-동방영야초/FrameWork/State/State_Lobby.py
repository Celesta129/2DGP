from pico2d import *
from FrameWork import MainFrameWork

image_Lobby = None

name = "State_Lobby"

def enter():
    global image_Lobby
    image_Lobby = load_image("Menu.png")

    if (image_Lobby == None):
        a = 1

    pass


def exit():
    global image_Lobby
    del(image_Lobby)



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
    global image_Lobby
    clear_canvas()
    #image_Lobby.clip_draw(14,528,800,600,400,300,1400,810)
    update_canvas()
    pass