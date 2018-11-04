from pico2d import *
from FrameWork import MainFrameWork
from FrameWork import CObject
from FrameWork import Game_World
name = "class_CEnemy"
#FRAMES_PER_ACTION
#ACTION_PER_TIME
#game_framework.frame_time) % 8


class Zaco1:
    enemy_image = None
    left = 10
    bottom = 38

    width = 20
    height = 24

    image_width = 32
    image_height = 32
    max_frame = 4


    def __init__(self,x = None,y = None):
        if Zaco1.enemy_image == None:
            Zaco1.enemy_image = load_image("Enemies & Special Projectiles.png")

        self.ObjectInfo = CObject.cObject()

        self.ObjectInfo.image = Zaco1.enemy_image
        self.ObjectInfo.x,self.ObjectInfo.y = 0,0
        if (None != x): self.ObjectInfo.x = x
        if (None != y): self.ObjectInfo.y = y

        self.ObjectInfo.image_left, self.ObjectInfo.image_bottom = Zaco1.left, Zaco1.enemy_image.h - Zaco1.bottom
        self.ObjectInfo.width,self.ObjectInfo.height = Zaco1.width, Zaco1.height
        self.ObjectInfo.image_width, self.ObjectInfo.image_height = Zaco1.image_width, Zaco1.image_height

        self.ObjectInfo.frame = 0
        self.ObjectInfo.max_frame = Zaco1.max_frame

        self.ObjectInfo.objectType = "Rect"

        self.shot_pattern = SP_1
        self.bullet = None

        self.hp = 10

        self.shot_timer_max = 0.5
        self.shot_timer = 0.5
        pass

    def update(self):
        MAX_FRAME =  self.ObjectInfo.max_frame
        TIME_PER_ACTION = 0.5
        ACTION_PER_TIME = 1.0 / TIME_PER_ACTION


        self.shot_timer -= MainFrameWork.frame_time
        if(self.shot_timer <= 0.0):
            self.shot_timer = self.shot_timer_max

        self.shot_pattern.shot(self)
        self.ObjectInfo.frame = (self.ObjectInfo.frame + MAX_FRAME * ACTION_PER_TIME * MainFrameWork.frame_time) % MAX_FRAME

        pass

    def draw(self):
        self.ObjectInfo.draw()
        pass

    def shot(self,bullet):
        Game_World.add_bullet(bullet,Game_World.layer_eTp)
        pass

    def pattern_change(self,shot_pattern):
        self.shot_pattern.exit(self)
        self.shot_pattern = shot_pattern
        self.shot_pattern.enter(self)
    pass

class SP_1:
    @staticmethod
    def enter(Enemy):
        pass

    def exit(Enemy):
        pass

    @staticmethod
    def shot(Enemy):
        newBullet = Enemy.bullet
        # 여기서 필요한 조정
        #Enemy.shot(newBullet)   # 만든 탄환을 레이어에 집어넣기만 하는 함수임.
    pass

class bullet1:
    def draw(self):
        pass

    pass