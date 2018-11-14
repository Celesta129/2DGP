from pico2d import *
from FrameWork import MainFrameWork, CEnemy
from FrameWork.State import State_Pause
from FrameWork.CPlayer import cPlayer
from FrameWork import Game_World
from FrameWork.Calculator import *
name = "State_Stage"

image_Main_BG = None
image_Background = None

Stage_image = None
Stage_Scroll_y = 0

image_sidebar = None

player = None
test_enemy = None

STAGE1,STAGE2 = range(2)
stage_pos_table = {STAGE1:(17,292,258,258),STAGE2:(17,929,255,255)}
cur_stage_number = STAGE1

def enter():
    global image_Main_BG
    global player
    global Stage_image
    global image_sidebar
    global test_enemy
    if player == None:
        player = cPlayer(240,100)

        pass
    if test_enemy == None:
        test_enemy = CEnemy.Zaco_Blue(240,500)
    if image_Main_BG == None:
        image_Main_BG = load_image("MainBackGround.png")
    if Stage_image == None:
        Stage_image = load_image("Stage Character Background Text.png")
    if image_sidebar == None:
        image_sidebar = load_image("Sidebar & Pause Screen.png")

    player.x,player.y = 240,100
    Game_World.add_object(player, Game_World.layer_player)
    Game_World.add_object(test_enemy, Game_World.layer_enemy)
def exit():
    Game_World.clear()
    Game_World.clear_bullet()
    pass

def pause():
    global player
    player.velocity = [0,0]
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            MainFrameWork.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            MainFrameWork.push_state(State_Pause)
        else:
            player.handle_event(event)
    pass


def update():
    for object in Game_World.all_objects():
        object.update()
    for bullet in Game_World.all_bullets():
        bullet.update()

    bullet_collision()

    pass
def bullet_collision():
    # 충돌체크
    # playerBullet to Enemy
    for bullet in Game_World.bullets[Game_World.layer_pTe]:
        for enemy in Game_World.objects[Game_World.layer_enemy]:
            if True == collision(bullet, enemy):
                print("pTe Bullet Collision")
                Game_World.remove_bullet(bullet)
                enemy.hp -= bullet.dmg

    # enemyBullet to Player
    for bullet in Game_World.bullets[Game_World.layer_eTp]:
        for player in Game_World.objects[Game_World.layer_player]:
            if True == collision(bullet, player):
                print("eTp Bullet Collision")
                Game_World.remove_bullet(bullet)

    # 몹의 체력이 0이라면 삭제
    for enemy in Game_World.objects[Game_World.layer_enemy]:
        if enemy.hp <= 0:
            Game_World.remove_object(enemy)
            print("delete Enemy")

    # 화면 나가면 삭제
    for bullet in Game_World.all_bullets():
        if True == test_Background_coll(bullet):
            Game_World.remove_bullet(bullet)

def test_Background_coll(object):
    stage_width = 480
    stage_height = 550

    stage_bottom = 290 - stage_height * 0.5
    stage_left = 250 - stage_width * 0.5
    stage_top = stage_bottom + stage_height
    stage_right = stage_left + stage_width

    if object.y + object.height * 0.5 < stage_bottom \
            or object.y - object.height * 0.5 > stage_top:
       return True

    elif object.x + object.width * 0.5 < stage_left \
            or object.x - object.width * 0.5 > stage_right:
        return True

    return False

def draw():
    global image_Main_BG
    clear_canvas()
    draw_background()
    draw_scoreboard()
    for object in Game_World.all_objects():
        object.draw()
    for bullet in Game_World.all_bullets():
        bullet.draw()
    draw_cover()
    update_canvas()
    pass

scroll = 0
scroll_speed = 0

def draw_background():
    global scroll
    image_Main_BG.clip_draw(0, 0, 121, 159, 400, 300, 800, 600)

    left = stage_pos_table[cur_stage_number][0]
    bottom = Stage_image.h - stage_pos_table[cur_stage_number][1]
    width = stage_pos_table[cur_stage_number][2]
    height = stage_pos_table[cur_stage_number][3]

    scroll = (scroll + 1) % height
    x,y = 250,290
    Stage_image.clip_draw(left,bottom,width,height,x,y, 480, 550)

def draw_cover():
    #cap
    x = 250
    y = 290 + 275 + 17.5
    width,height = 480,35
    image_Main_BG.clip_draw(0, 0, 121, 159, x, y, width, height)

    # bottom
    x = 400
    y = 7.5
    width = 800
    height = 15
    image_Main_BG.clip_draw(0, 0, 121, 159, x, y, width, height)


    # right
    x = 250 + 230 + 35
    y = 290
    width = 70
    height = 600
    image_Main_BG.clip_draw(0, 0, 121, 159, x, y, width, height)
    #left
    x = 250 - 230 - 10
    y = 290
    width, height = 20, 600
    image_Main_BG.clip_draw(0, 0, 121, 159, x, y, width, height)

def draw_scoreboard():
    logo_width = 130
    logo_height = 238
    logo_left = 435
    logo_bottom = image_sidebar.h - 273
    image_width = logo_width * 1.3
    image_height = logo_height * 1.3

    image_sidebar.clip_draw(logo_left,logo_bottom,logo_width,logo_height,650,200,image_width,image_height )
    pass