from pico2d import *
import game_framework
import game_world

import world_build_state
import boy

def enter():
    # game world is prepared already in world_build_state
    global boy
    boy = world_build_state.get_boy()
    pass

def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(world_build_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            game_world.save()


def update():
   pass

def draw():
    clear_canvas()
    game_framework.stack[-2].draw()

    update_canvas()
