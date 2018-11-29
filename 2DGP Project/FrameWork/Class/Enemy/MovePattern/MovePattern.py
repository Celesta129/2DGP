from FrameWork import Game_World
from FrameWork.Calculator import*

class MP_go_straight:

    @staticmethod
    def enter(Enemy):
        Enemy.velocity[0] = 0.0
        Enemy.velocity[1] = -10.0 # km/h
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


