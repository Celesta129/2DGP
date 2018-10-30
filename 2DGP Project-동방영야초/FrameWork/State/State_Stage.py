from pico2d import *
from FrameWork import MainFrameWork
from FrameWork.CPlayer import cPlayer
from FrameWork import Game_World

name = "State_Stage"

image_Main_BG = None
image_Background = None

Stage_image = None
Stage_Scroll_y = 0

player = None


def enter():
    global image_Main_BG
    global player
    global Stage_image
    if player == None:
        player = cPlayer(400,300)
        Game_World.add_object(player,Game_World.layer_object)
        pass
    if image_Main_BG == None:
        image_Main_BG = load_image("MainBackGround.png")
    if Stage_image == None:
        Stage_image = load_image("Stage Character Background Text.png")

def exit():
    global image_Main_BG
    global player
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

        else:
            for i in range(Game_World.layer_end):
                for object in Game_World.objects[i]:
                    object.handle_event(event)
    pass


def update():

    for i in range(Game_World.layer_end):
        for object in Game_World.objects[i]:
            object.update()

    pass


def draw():
    global image_Main_BG
    clear_canvas()

    image_Main_BG.clip_draw(0,0,121,159,400,300,800,600)
    for i in range(Game_World.layer_end):
        for object in Game_World.objects[i]:
            object.draw()
    update_canvas()
    pass