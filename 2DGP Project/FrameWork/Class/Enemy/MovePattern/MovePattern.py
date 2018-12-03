from FrameWork import Game_World
from FrameWork.Calculator import*
from FrameWork.Class.Enemy.EnemyClass.BulletGenerator import *
from FrameWork.Class.Enemy.ShotPattern.ShotPattern import *
class MP_go_straight:

    @staticmethod
    def enter(Enemy):
        Enemy.velocity[0] = 0.0
        Enemy.velocity[1] = -20.0 # km/h
        pass

    @staticmethod
    def exit(Enemy):
        pass

    @staticmethod
    def update(Enemy):
        Enemy.move()
        pass

class MP_go_right:
    @staticmethod
    def enter(Enemy):
        Enemy.velocity[0] = 20.0
        Enemy.velocity[1] = 0.0  # km/h
        pass

    @staticmethod
    def exit(Enemy):
        pass
    @staticmethod
    def update(Enemy):
        Enemy.move()
        pass

class MP_go_left:
    @staticmethod
    def enter(Enemy):
        Enemy.velocity[0] = -20.0
        Enemy.velocity[1] = 0.0  # km/h
        pass

    @staticmethod
    def exit(Enemy):
        pass

    @staticmethod
    def update(Enemy):
        Enemy.move()
        pass

class MP_Boss_Move1:
    @staticmethod
    def enter(Boss):
        Boss.velocity[0] = 0.0
        Boss.velocity[1] = -20.0  # km/h
        pass

    @staticmethod
    def exit(Boss):

        pass

    @staticmethod
    def update(Boss):
        if Boss.y > 400:
            Boss.move()
        elif Boss.shot_pattern == None :
            Boss.change_shot_pattern(SP_Boss1)

        if Boss.cur_move_pattern_time >= 9:
            Boss.change_move_pattern(MP_Boss_Move2)
        pass

# 우상단으로 이동
class MP_Boss_Move2:
    @staticmethod
    def enter(Boss):
        Boss.velocity[0] = 15.0
        Boss.velocity[1] = 10.0  # km/h
        pass

    @staticmethod
    def exit(Enemy):
        pass

    @staticmethod
    def update(Boss):
        if Boss.y < 500:
            Boss.move()

        if Boss.cur_move_pattern_time >= 9:
            Boss.change_move_pattern(MP_Boss_Move3)
        pass

class MP_Boss_Move3:
    @staticmethod
    def enter(Boss):
        Boss.velocity[0] = -15.0
        Boss.velocity[1] = -10.0  # km/h
        pass

    @staticmethod
    def exit(Enemy):
        pass

    @staticmethod
    def update(Boss):
        if Boss.y > 400:
            Boss.move()

        if Boss.cur_move_pattern_time >= 9:
            Boss.change_move_pattern(MP_Boss_Move2)
        pass