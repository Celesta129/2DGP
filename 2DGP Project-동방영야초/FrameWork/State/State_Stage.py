from pico2d import *
from FrameWork import MainFrameWork
from FrameWork.CPlayer import cPlayer
from FrameWork import Game_World

name = "State_Stage"

image_Main_BG = None
image_Background = None

Stage_image = None
Stage_Scroll_y = 0

image_sidebar = None

player = None

STAGE1,STAGE2 = range(2)
stage_pos_table = {STAGE1:(17,292,258,258),STAGE2:(17,929,255,255)}
cur_stage_number = STAGE1

def enter():
    global image_Main_BG
    global player
    global Stage_image
    global image_sidebar
    if player == None:
        player = cPlayer(400,300)
        Game_World.add_object(player,Game_World.layer_object)
        pass
    if image_Main_BG == None:
        image_Main_BG = load_image("MainBackGround.png")
    if Stage_image == None:
        Stage_image = load_image("Stage Character Background Text.png")
    if image_sidebar == None:
        image_sidebar = load_image("Sidebar & Pause Screen.png")
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
            player.handle_event(event)
    pass


def update():
    for object in Game_World.all_objects():
        object.update()
    for bullet in Game_World.all_bullets():
        bullet.update()

    pass


def draw():
    global image_Main_BG
    clear_canvas()

    draw_background()
    draw_scoreboard()
    for object in Game_World.all_objects():
        object.draw()
    for bullet in Game_World.all_bullets():
        bullet.draw()
    update_canvas()
    pass

def draw_background():
    image_Main_BG.clip_draw(0, 0, 121, 159, 400, 300, 800, 600)

    left = stage_pos_table[cur_stage_number][0]
    bottom = Stage_image.h - stage_pos_table[cur_stage_number][1]
    width = stage_pos_table[cur_stage_number][2]
    height = stage_pos_table[cur_stage_number][3]

    x,y = 250,290
    Stage_image.clip_draw(left,bottom,width,height,x,y, 480, 550)



def draw_scoreboard():
    logo_width = 130
    logo_height = 238
    logo_left = 435
    logo_bottom = image_sidebar.h - 273
    image_width = logo_width * 1.3
    image_height = logo_height * 1.3

    image_sidebar.clip_draw(logo_left,logo_bottom,logo_width,logo_height,650,200,image_width,image_height )
    pass