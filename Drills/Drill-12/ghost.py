from pico2d import *
import math
import game_framework
import random

PIXEL_PER_METER = 10.0 / 0.3
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000.0 / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER


# 단위원에서의 각 변화량 theta, 각속도 w일때
# theta = w * t
# w = theta / t
# t는 매 프레임마다 다르다. t = game_framework.frame_time
# 따라서 w는 매 프레임마다 바뀐다.

# 결론 : 각속도 w = fAngle / 1 * game_framework.frame_time
# 가속도 A = -w**2 * 원점에서의 위치벡터
# v = v0 + a
# pos = pos0 + v

fAngle = 4 * math.pi



#meter
Radius = 3 * PIXEL_PER_METER

class cGhost:
    image_boy = None
    def __init__(self,x,y):
        self.x,self.y = x,y
        #회전 중심으로부터의 상대위치. 초기값은 Radius만큼 나가야할것임. 연출때문에 0으로 설정.

        self.rx,self.ry = 0,0
        self.bSwitch = False

        w = fAngle / 1 * game_framework.frame_time
        # 초기값에서의 속도(위치 미분)
        self.velocity_x = Radius * w
        self.velocity_y = 0.0

        if(None == cGhost.image_boy):
            cGhost.image_boy = load_image('animation_sheet.png')
        pass

    def draw(self):
        cGhost.image_boy.clip_draw(0,300,100,100,self.x + self.rx ,self.y + self.ry)
        pass

    def cal_velocity(self):
        w = fAngle / 1 * game_framework.frame_time

        self.rx += self.velocity_x
        self.ry += self.velocity_y

        acc_x = -w**2 * self.rx
        acc_y = -w**2 * self.ry

        self.velocity_x += acc_x
        self.velocity_y += acc_y

    def update(self):
        if self.bSwitch == True:
            self.cal_velocity()
        else:
            self.ry += Radius * 0.005
            opacity = random.randint(1, 50) * 0.01
            cGhost.image_boy.opacify(opacity)
            if(self.ry == Radius):
                self.bSwitch = True
                cGhost.image_boy.opacify(0.7)


        pass

    pass