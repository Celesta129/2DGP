from pico2d import *
from FrameWork import MainFrameWork
from FrameWork.CObject import *
from FrameWork import Game_World
from FrameWork.Calculator import *
from FrameWork.CBullet import *
from FrameWork.Class.Enemy.ShotPattern.ShotPattern import *
from FrameWork.Class.Enemy.MovePattern.MovePattern import *
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

        self.cur_shot_pattern_time = 0.0
        self.shot_timer = 0.0
        self.shot_timer_max = 0.0

        self.shot_pattern = SP_Aiming
        #SP_Aiming
        #SP_3way_Shot
        self.change_shot_pattern(SP_Aiming)
        self.bullet = eBullet_rice_blue

        self.cur_move_pattern_time = 0.0
        self.move_pattern = MP_go_straight
        self.change_move_pattern(MP_go_straight)

        self.hp = 10

    @staticmethod
    def create(x, y):
        return Zaco_Blue(x, y)

    def update(self):
        MAX_FRAME =  self.max_frame
        TIME_PER_ACTION = 0.5
        ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

        self.frame = (self.frame + MAX_FRAME * ACTION_PER_TIME * MainFrameWork.frame_time) % MAX_FRAME

        self.cur_move_pattern_time += MainFrameWork.frame_time
        self.cur_shot_pattern_time += MainFrameWork.frame_time
        self.shot_timer -= MainFrameWork.frame_time

        self.move_pattern.update(self)
        if self.shot_timer <= 0.0 and self.check_cycle():
            self.shot_timer = self.shot_timer_max
            self.shot_pattern.shot(self)

    def check_cycle(self):
        if self.cur_shot_pattern_time % self.shot_pattern.pattern_cycle < self.shot_pattern.pattern_breaktime:
            return False
        return True

    def shoot(self,bullet):
        Game_World.add_bullet(bullet,Game_World.layer_eTp)
        pass

    def change_shot_pattern(self,shot_pattern):
        self.cur_shot_pattern_time = 0.0

        self.shot_pattern.exit(self)
        self.shot_pattern = shot_pattern
        self.shot_pattern.enter(self)

    def change_move_pattern(self,move_pattern):
        self.cur_move_pattern_time = 0.0

        self.move_pattern.exit(self)
        self.move_pattern = move_pattern
        self.move_pattern.enter(self)

