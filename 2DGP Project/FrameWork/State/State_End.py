from pico2d import *
from FrameWork import MainFrameWork
from FrameWork.State import State_Stage

image_Exit = None

Logo_left = 1092
Logo_bottom = 998
Logo_width,Logo_height = 220,380
name = "State_Lobby"

def enter():
    global image_Exit

    if (image_Exit == None):
        image_Exit = load_image("End.png")


def exit():
    global image_Exit
    del(image_Exit)



def pause():
    pass


def resume():
    pass


def handle_events():
    global button_select
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            MainFrameWork.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            MainFrameWork.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE :
                MainFrameWork.quit()
    pass


def update():
    pass


def draw():
    global image_Exit
    clear_canvas()

    draw_background()

    update_canvas()


def draw_background():
    image_Exit.clip_draw(0,0,800,600,400,300)
