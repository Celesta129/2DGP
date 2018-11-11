from pico2d import *
from FrameWork import MainFrameWork
from FrameWork.CObject import *
from FrameWork import Game_World
from FrameWork import Calculator
from FrameWork.CBullet import *
name = "class_CEnemy"
#FRAMES_PER_ACTION
#ACTION_PER_TIME
#game_framework.frame_time) % 8


class Zaco1(cObject):

    enemy_image = None
    left = 10
    bottom = 38

    width = 20
    height = 24

    image_width = 32
    image_height = 32
    max_frame = 4


    def __init__(self,x = None,y = None):
        super().__init__(x,y)
        if Zaco1.enemy_image == None:
            Zaco1.enemy_image = load_image("Enemies & Special Projectiles.png")


        self.image = Zaco1.enemy_image


        self.image_left, self.image_bottom = Zaco1.left, Zaco1.enemy_image.h - Zaco1.bottom
        self.width,self.height = Zaco1.width, Zaco1.height
        self.image_width, self.image_height = Zaco1.image_width, Zaco1.image_height

        self.frame = 0
        self.max_frame = Zaco1.max_frame

        self.objectType = "Rect"

        self.shot_pattern = SP_2
        self.bullet = eBullet_1

        self.hp = 10

        self.shot_timer_max = 1.0
        self.shot_timer = 1.0
        pass

    def update(self):
        MAX_FRAME =  self.max_frame
        TIME_PER_ACTION = 0.5
        ACTION_PER_TIME = 1.0 / TIME_PER_ACTION


        self.shot_timer -= MainFrameWork.frame_time
        if(self.shot_timer <= 0.0):
            self.shot_timer = self.shot_timer_max
            self.shot_pattern.shot(self)

        self.frame = (self.frame + MAX_FRAME * ACTION_PER_TIME * MainFrameWork.frame_time) % MAX_FRAME

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
        if(Enemy.bullet == None):
            pass

        target = Game_World.objects[Game_World.layer_player][0]
        newBullet = Enemy.bullet(Enemy.x,Enemy.y)


        # 일단 플레이어쪽으로 쏴보자
        rot = math.degrees(Calculator.get_angle_down(Enemy,target))
        # 여기서 필요한 조정
        InitBullet(newBullet, rot, 50, 50)
        Enemy.shot(newBullet)   # 만든 탄환을 레이어에 집어넣기만 하는 함수임.
    pass

class SP_2: # 3way shot
    @staticmethod
    def enter(Enemy):
        pass

    def exit(Enemy):
        pass

    @staticmethod
    def shot(Enemy):
        if (Enemy.bullet == None):
            pass

        target = Game_World.objects[Game_World.layer_player][0]
        BulletList = [Enemy.bullet(Enemy.x, Enemy.y) for i in range(3)]

        InitNWayBullet(BulletList,0,-50,30)
        # 여기서 필요한 조정
        for Bullet in BulletList:
            Enemy.shot(Bullet)  # 만든 탄환을 레이어에 집어넣기만 하는 함수임.