from FrameWork import Game_World
from FrameWork.Calculator import*
from FrameWork.CBullet import *

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