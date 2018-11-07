from pico2d import *
from FrameWork import MainFrameWork
from FrameWork import Game_World

def enter():
    pass
def exit():
    pass

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

def draw():
    pass

def update():
    pass

