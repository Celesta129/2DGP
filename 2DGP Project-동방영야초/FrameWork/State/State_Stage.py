from pico2d import *
from FrameWork import MainFrameWork
from FrameWork.CPlayer import cPlayer

name = "State_Stage"

image_Main_BG = None
image_Background = None

Stage_image = None
Stage_Scroll_y = 0

player = None

list_objects = []
list_pTe = []
list_eTp = []

def enter():
    global image_Main_BG
    global player
    global Stage_image
    if player == None:
        player = cPlayer(400,300)
        pass
    if image_Main_BG == None:
        image_Main_BG = load_image("MainBackGround.png")
    if Stage_image == None:
        Stage_image = load_image("Stage Character Background Text.png")

def exit():
    global image_Main_BG
    global player
    del(image_Main_BG)
    del(player)



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
            player.handle_event(event)
    pass


def update():
    global list_pTe
    global list_eTp

    player.update(list_pTe)
    for object in list_objects:
        object.update(list_eTp)

    for bullet in list_pTe:
        bullet.update()
    for bullet in list_eTp:
        bullet.update()

    i = 0
    for bullet in list_pTe:
        if list_pTe[i].ObjectInfo.y >= 650 or list_pTe[i].ObjectInfo.y <= -50:
            _bullet = list_pTe.pop(i)
            del(_bullet)
        i += 1
    i = 0
    for bullet in list_eTp:
        if list_eTp[i].ObjectInfo.y >= 650 or list_eTp[i].ObjectInfo.y <= -50:
            _bullet = list_eTp.pop(i)
            del (_bullet)
        i += 1
    pass


def draw():
    global image_Main_BG
    global list_pTe
    global list_eTp
    clear_canvas()

    image_Main_BG.clip_draw(0,0,121,159,400,300,800,600)
    player.draw()
    for bullet in list_pTe:
        bullet.draw()
    for bullet in list_eTp:
        bullet.draw()
    update_canvas()
    pass