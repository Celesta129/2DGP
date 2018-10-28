from pico2d import *
from FrameWork import MainFrameWork


name = "State_Logo"

image_logo = None

image_width = None
image_height = None

Logo_x = None
Logo_y = None

def enter():
    global image_logo
    global image_height
    global image_width
    global Logo_x
    global Logo_y

    if image_logo == None:
        image_logo = load_image("Menu.png")
        image_width = image_logo.w
        image_height = image_logo.h
        Logo_x = 688
        Logo_y = image_height - 529

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

    image_logo.clip_draw(687,Logo_y,640,480,400,300,800,600)

    update_canvas()
    pass