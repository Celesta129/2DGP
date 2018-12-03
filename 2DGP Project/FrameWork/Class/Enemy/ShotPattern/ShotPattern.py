from FrameWork import Game_World
from FrameWork.Calculator import*
from FrameWork.CBullet import *

class SP_Aiming_BlueWedge:
    pattern_cycle = 1.5
    pattern_breaktime = 1.0
    color = BLUE1

    @staticmethod
    def enter(Enemy):
        Enemy.shot_timer = 0.1
        Enemy.shot_timer_max = 0.1
        pass

    def exit(Enemy):
        pass

    @staticmethod
    def shot(Enemy):

        target = Game_World.objects[Game_World.layer_player][0]
        newBullet = Bullet_Wedge(Enemy.x,Enemy.y, SP_Aiming_BlueWedge.color)

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

class SP_360_bum_smallrice:
    pattern_cycle = 1.5
    pattern_breaktime = 1.0
    color = YELLOW3
    def enter(Enemy):
        Enemy.shot_timer = 0.3
        Enemy.shot_timer_max = 0.3
        pass

    def exit(Enemy):
        pass

    @staticmethod
    def shot(Enemy):
        target = Game_World.objects[Game_World.layer_player][0]
        newBullet = Bullet_SmallRice(Enemy.x, Enemy.y, SP_360_bum_smallrice.color)

        # 일단 플레이어쪽으로 쏴보자
        rot = math.degrees(get_angle_down(Enemy, target))
        bulletlist = [Bullet_SmallRice(Enemy.x, Enemy.y,SP_360_bum_smallrice.color) for i in range(21)]

        InitNWayBullet(bulletlist,0,-50,360/21)
        # 여기서 필요한 조정
        for bullet in bulletlist:
            Enemy.shoot(bullet)

class SP_back_blueCircle:
    # Enemy need Bullet Generator
    pattern_cycle = 1.5
    pattern_breaktime = 1.0
    color = BLUE1

    def enter(Enemy):
        Enemy.shot_timer = 0.3
        Enemy.shot_timer_max = 0.3
        pass

    def exit(Enemy):
        pass

    @staticmethod
    def shot(Enemy):
        target = Game_World.objects[Game_World.layer_player][0]
        #newBullet = Bullet_Circle(Enemy.x, Enemy.y, SP_back_blueCircle.color)

        # 일단 플레이어쪽으로 쏴보자

        for generator in Enemy.bullet_generators :
            bullet = Bullet_Circle(generator.x, generator.y, SP_back_blueCircle.color)
            radian = math.radians(generator.rot + 90)
            speed = 30
            bullet.velocity[0] = (math.cos(radian) - math.sin(radian)) * speed
            bullet.velocity[1] = (math.sin(radian) + math.cos(radian)) * speed
            # 여기서 필요한 조정
            Enemy.shoot(bullet)