from pico2d import *
from FrameWork import MainFrameWork

image_Lobby = None

name = "State_Lobby"

def enter():
    global image_Lobby

    if (image_Lobby == None):
        image_Lobby = load_image("Menu.png")


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

    draw_background()

    update_canvas()


def draw_background():
    if image_Lobby != None:
        image_Lobby.clip_draw(14, image_Lobby.h - 529, 640, 480, 400, 300, 800, 600)