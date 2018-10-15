import game_framework
from pico2d import *
import title_state

name = "PauseState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del (image)


def update():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()


def draw():
    global image
    clear_canvas()
    #game_framework.stack[-2].draw()
    image.draw(400,300)
    #image.clip_draw(0, 0, 900, 900, 400, 300)
    update_canvas()


def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass