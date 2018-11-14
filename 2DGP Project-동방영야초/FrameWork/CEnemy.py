from pico2d import *
from FrameWork import MainFrameWork
from FrameWork.CObject import *
from FrameWork import Game_World
from FrameWork.Calculator import *
from FrameWork.CBullet import *
name = "class_CEnemy"
#FRAMES_PER_ACTION
#ACTION_PER_TIME
#game_framework.frame_time) % 8


class Zaco_Blue(Object):

    enemy_image = None
    LEFT = 10
    BOTTOM = 38

    WIDTH = 20
    HEIGHT = 24

    IMAGE_WIDTH = 32
    IMAGE_HEIGHT = 32
    MAX_FRAME = 4

    def __init__(self,x = None,y = None):
        super().__init__(x,y)
        if Zaco_Blue.enemy_image == None:
            Zaco_Blue.enemy_image = load_image("Enemies & Special Projectiles.png")

        self.image = Zaco_Blue.enemy_image

        self.image_left, self.image_bottom = Zaco_Blue.LEFT, Zaco_Blue.enemy_image.h - Zaco_Blue.BOTTOM
        self.width,self.height = Zaco_Blue.WIDTH, Zaco_Blue.HEIGHT
        self.image_width, self.image_height = Zaco_Blue.IMAGE_WIDTH, Zaco_Blue.IMAGE_HEIGHT

        self.frame = 0
        self.max_frame = Zaco_Blue.MAX_FRAME

        self.objectType = "Rect"

        self.shot_timer = 0.0
        self.cur_pattern_time = 0.0
        self.shot_timer_max = 0.0

        self.shot_pattern = SP_Aiming
        #SP_Aiming
        #SP_3way_Shot
        self.change_pattern(SP_3way_Shot)
        self.bullet = eBullet_rice_blue

        self.hp = 10

    def update(self):
        MAX_FRAME =  self.max_frame
        TIME_PER_ACTION = 0.5
        ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

        self.frame = (self.frame + MAX_FRAME * ACTION_PER_TIME * MainFrameWork.frame_time) % MAX_FRAME

        self.cur_pattern_time += MainFrameWork.frame_time
        self.shot_timer -= MainFrameWork.frame_time


        if self.shot_timer <= 0.0 and self.check_cycle():
            self.shot_timer = self.shot_timer_max
            self.shot_pattern.shot(self)

    def check_cycle(self):
        if self.cur_pattern_time % self.shot_pattern.pattern_cycle < self.shot_pattern.pattern_breaktime:
            return False
        return True
    def shoot(self,bullet):
        Game_World.add_bullet(bullet,Game_World.layer_eTp)
        pass

    def change_pattern(self,shot_pattern):
        self.cur_pattern_time = 0.0

        self.shot_pattern.exit(self)
        self.shot_pattern = shot_pattern
        self.shot_pattern.enter(self)


class SP_Aiming:
    pattern_cycle = 1.5
    pattern_breaktime = 0.5
    @staticmethod
    def enter(Enemy):
        Enemy.shot_timer = 0.15
        Enemy.shot_timer_max = 0.15
        pass

    def exit(Enemy):
        pass

    @staticmethod
    def shot(Enemy):

        target = Game_World.objects[Game_World.layer_player][0]
        newBullet = Enemy.bullet(Enemy.x,Enemy.y)

        # 일단 플레이어쪽으로 쏴보자
        rot = math.degrees(get_angle_down(Enemy,target))
        # 여기서 필요한 조정
        InitBullet(newBullet, rot, 50, 50)
        Enemy.shoot(newBullet)   # 만든 탄환을 레이어에 집어넣기만 하는 함수임.
    pass

class SP_3way_Shot:
    pattern_cycle = 1.5
    pattern_breaktime = 0.5
    @staticmethod
    def enter(Enemy):
        Enemy.shot_timer = 0.1
        Enemy.shot_timer_max = 0.1
        pass

    def exit(Enemy):
        pass

    @staticmethod
    def shot(Enemy):
        if Enemy.bullet == None:
            pass

        target = Game_World.objects[Game_World.layer_player][0]
        bulletlist = [Enemy.bullet(Enemy.x, Enemy.y) for i in range(3)]

        InitNWayBullet(bulletlist,0,-55, 30)
        rotate_bullet(bulletlist,90)
        # 여기서 필요한 조정
        for bullet in bulletlist:
            Enemy.shoot(bullet)  # 만든 탄환을 레이어에 집어넣기만 하는 함수임.