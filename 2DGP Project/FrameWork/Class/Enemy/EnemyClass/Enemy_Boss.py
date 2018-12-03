from pico2d import *
from FrameWork.State.State_Stage import *

from FrameWork import MainFrameWork
from FrameWork.CObject import *
from FrameWork import Game_World
from FrameWork.Calculator import *
from FrameWork.CBullet import *
from FrameWork.Class.Enemy.ShotPattern.ShotPattern import *
from FrameWork.Class.Enemy.MovePattern.MovePattern import *
name = "class_Boss"
#FRAMES_PER_ACTION
#ACTION_PER_TIME
#game_framework.frame_time) % 8


class Boss(Object):

    enemy_image = None
    LEFT = 581
    BOTTOM = 1943

    WIDTH = 53
    HEIGHT = 60

    IMAGE_WIDTH = 53
    IMAGE_HEIGHT = 60
    MAX_FRAME = 1

    def __init__(self,x ,y, move_pattern, shot_pattern):
        global bgm

        super().__init__(x,y)
        if Boss.enemy_image == None:
            Boss.enemy_image = load_image("Stage Character Background Text.png")

        self.image = Boss.enemy_image

        self.image_left, self.image_bottom = Boss.LEFT, Boss.enemy_image.h - Boss.BOTTOM
        self.width,self.height = Boss.WIDTH, Boss.HEIGHT
        self.image_width, self.image_height = Boss.IMAGE_WIDTH, Boss.IMAGE_HEIGHT

        self.frame = 0
        self.max_frame = Boss.MAX_FRAME

        self.objectType = "Rect"

        #현재 사격패턴에 들어간 시간
        self.cur_shot_pattern_time = 0.0
        #한 발의 사격에 필요한 시간
        self.shot_timer = 0.0
        # 타이머 초기화값
        self.shot_timer_max = 0.0

        self.shot_pattern = shot_pattern
        self.change_shot_pattern(shot_pattern)

        self.cur_move_pattern_time = 0.0
        self.move_pattern = move_pattern
        self.change_move_pattern(move_pattern)

        self.hp = 500

        self.bullet_generators = []
        bgm = load_music("Master_Spark.mp3")
        bgm.repeat_play()
    def update(self):
        MAX_FRAME =  self.max_frame
        TIME_PER_ACTION = 0.5
        ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

        self.frame = (self.frame + MAX_FRAME * ACTION_PER_TIME * MainFrameWork.frame_time) % MAX_FRAME

        self.cur_move_pattern_time += MainFrameWork.frame_time
        self.cur_shot_pattern_time += MainFrameWork.frame_time
        self.shot_timer -= MainFrameWork.frame_time

        self.move_pattern.update(self)
        for generator in self.bullet_generators:
            generator.update()

        if self.shot_timer <= 0.0 and self.shot_pattern != None and self.check_cycle():
            self.shot_timer = self.shot_timer_max
            self.shot_pattern.shot(self)

    def draw(self):
        for generator in self.bullet_generators:
            generator.draw()
        super().draw()


    def check_cycle(self):
        if self.cur_shot_pattern_time % self.shot_pattern.pattern_cycle < self.shot_pattern.pattern_cycle - self.shot_pattern.pattern_breaktime:
            return False
        return True

    def shoot(self,bullet):
        Game_World.add_bullet(bullet,Game_World.layer_eTp)
        pass

    def change_shot_pattern(self,shot_pattern):
        self.hp = 500
        self.cur_shot_pattern_time = 0.0

        if self.shot_pattern != None:
            self.shot_pattern.exit(self)

        self.shot_pattern = shot_pattern
        if shot_pattern != None:
            self.shot_pattern.enter(self)

    def change_move_pattern(self,move_pattern):
        self.cur_move_pattern_time = 0.0

        self.move_pattern.exit(self)
        self.move_pattern = move_pattern
        self.move_pattern.enter(self)


