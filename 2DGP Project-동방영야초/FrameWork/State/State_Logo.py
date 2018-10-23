from pico2d import *
from FrameWork import MainFrameWork


name = "State_Logo"

image_logo = None


def enter():
    global image_logo
    image_logo = load_image("Menu.png")

    if (image_logo == None):
        a = 1

    pass


def exit():
    global image_logo
    del(image_logo)



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
    global image_logo
    clear_canvas()
    image_logo.clip_draw(688,500,800,600,400,300,860,810)
    update_canvas()
    pass