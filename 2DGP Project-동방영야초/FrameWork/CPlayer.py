from pico2d import *

from FrameWork import CObject
from FrameWork import MainFrameWork
from FrameWork.CBullet import *
from FrameWork import Game_World

# Player Events
RIGHT_DOWN, LEFT_DOWN, UP_DOWN, DOWN_DOWN, RIGHT_UP, LEFT_UP, UP_UP, DOWN_UP, Z_DOWN, Z_UP, X_DOWN, X_UP, SHIFT_DOWN, SHIFT_UP  = range(14)
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYDOWN, SDLK_z) : Z_DOWN,
    (SDL_KEYUP, SDLK_z): Z_UP,
    (SDL_KEYDOWN, SDLK_x) : X_DOWN,
    (SDL_KEYUP, SDLK_x): X_UP,
    (SDL_KEYDOWN, SDLK_LSHIFT) : SHIFT_DOWN,
    (SDL_KEYUP, SDLK_LSHIFT): SHIFT_UP,
}


SPEED_KMPH = 60.0          # 60 km/h
SPEED_MPM = SPEED_KMPH * 1000.0 / 60.0
SPEED_MPS = SPEED_MPM / 60.0
SPEED_PPS = SPEED_MPS * CObject.PIXEL_PER_METER # Pixel Per second


class IdleState:
    image_bottom = 59
    MAX_FRAME = 4
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    @staticmethod
    def enter(Player,event = None):
        Player.image_bottom = cPlayer.Player_image.h -IdleState.image_bottom
        pass

    @staticmethod
    def exit(Player,event = None):
        pass

    @staticmethod
    def do(Player):
        Player.frame = (Player.frame + MoveState.MAX_FRAME* MoveState.ACTION_PER_TIME * MainFrameWork.frame_time) % IdleState.MAX_FRAME

    @staticmethod
    def draw(Player):
        Player.draw()

class MoveState:
    image_bottom = 59 + 46
    MAX_FRAME = 7
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    @staticmethod
    def enter(Player,event = None):
        Player.image_bottom = cPlayer.Player_image.h - MoveState.image_bottom
        Player.frame = 0
        pass

    @staticmethod
    def exit(Player,event = None):
        Player.frame = 0
        pass

    @staticmethod
    def do(Player):
        if(Player.frame < MoveState.MAX_FRAME - 1):
            Player.frame = (Player.frame + MoveState.MAX_FRAME* MoveState.ACTION_PER_TIME * MainFrameWork.frame_time)

    @staticmethod
    def draw(Player):
        Player.draw()

next_state_table = {
# fill here
    IdleState: {RIGHT_UP : MoveState, LEFT_UP: MoveState,
                UP_UP : MoveState, DOWN_UP : MoveState,
                RIGHT_DOWN: MoveState, LEFT_DOWN: MoveState,
                UP_DOWN: MoveState, DOWN_DOWN: MoveState,
                Z_DOWN: IdleState, Z_UP: IdleState,
                X_DOWN: IdleState, X_UP: IdleState,
                SHIFT_DOWN: IdleState, SHIFT_UP: IdleState
                },

    MoveState: {RIGHT_UP : MoveState, LEFT_UP: MoveState,
                UP_UP : MoveState, DOWN_UP : MoveState,
                RIGHT_DOWN: MoveState, LEFT_DOWN: MoveState,
                UP_DOWN: MoveState, DOWN_DOWN: MoveState,
                Z_DOWN: MoveState, Z_UP: MoveState,
                X_DOWN: MoveState, X_UP: MoveState,
                SHIFT_DOWN: MoveState, SHIFT_UP: MoveState
                }

}



name = "class_Player"
class cPlayer(cObject):
    Player_image = None
    Range_image = None
    AttackRange = (90,258)

    def __init__(self,x,y):
        if cPlayer.Player_image == None:
            cPlayer.Player_image = load_image("Players.png")
        if(cPlayer.Range_image == None):
            cPlayer.Range_image = load_image("Projectiles and Items.png")

        super().__init__(x,y)

        self.image = cPlayer.Player_image
        self.image_width = 32
        self.image_height = 46

        self.width = 24
        self.height = 40

        self.image_left = 12
        self.image_bottom = cPlayer.Player_image.h - 13
        self.max_frame = 4

        self.event_que = []
        self.cur_state = IdleState

        self.bshot = False
        self.bslow = False

        self.shot_timer_max = 0.05
        self.shot_timer = 0.00

        self.objectType = "Circle"
    def add_event(self, event):
        self.event_que.insert(0,event)

    def change_state(self,event):
        self.cur_state.exit(self, event)
        self.cur_state = next_state_table[self.cur_state][event]
        self.cur_state.enter(self, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0 :
            event = self.event_que.pop()
            self.change_state(event)

        if (self.velocity[0] > 0):
            self.flip = True
        elif self.velocity[0] == 0:
            self.cur_state.exit(self)
            self.cur_state = IdleState
            self.cur_state.enter(self)
        else:
            self.flip = False

        self.move()
        self.shot()

        if self.x - self.width*0.5 < 15:
            self.x = 15 + self.width*0.5
        elif self.x + self.width*0.5 > 480:
            self.x = 480 - self.width * 0.5

        if self.y - self.height * 0.5 < 15 :
            self.y = 15 + self.height * 0.5
        elif self.y + self.height * 0.5 > 565:
            self.y = 565 - self.height * 0.5
        # stage
        # 15 < x < 480
        # 20 <y< 565
        pass

    def shot(self):
        if self.bshot == True:
            if (self.shot_timer <= 0):
                Bullet = pBullet_1(self.x, self.y + 5)
                Init_Bullet(Bullet)
                Game_World.add_bullet(Bullet,Game_World.layer_pTe)
                self.shot_timer = self.shot_timer_max
                print('Shot')
            else:
                self.shot_timer -= MainFrameWork.frame_time
        else:
            self.shot_timer -= MainFrameWork.frame_time


    def handle_event(self,event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if key_event == RIGHT_DOWN:
                self.velocity[0] += SPEED_PPS
            elif key_event == LEFT_DOWN:
                self.velocity[0] -= SPEED_PPS
            elif key_event == UP_DOWN:
                self.velocity[1] += SPEED_PPS
            elif key_event == DOWN_DOWN:
                self.velocity[1] -= SPEED_PPS
            elif key_event == RIGHT_UP:
                self.velocity[0] -= SPEED_PPS
            elif key_event == LEFT_UP:
                self.velocity[0] += SPEED_PPS
            elif key_event == UP_UP:
                self.velocity[1] -= SPEED_PPS
            elif key_event == DOWN_UP:
                self.velocity[1] += SPEED_PPS
            elif key_event == Z_DOWN:
                self.bshot = True
            elif key_event == Z_UP:
                self.bshot = False
            elif key_event == SHIFT_DOWN:
                self.bslow = True
            elif key_event == SHIFT_UP:
                self.bslow = False
            self.add_event(key_event)

    def draw(self):
        cObject.draw(self)
        if self.bslow == True:
            cPlayer.Range_image.clip_draw(cPlayer.AttackRange[0],
                                      cPlayer.Range_image.h - cPlayer.AttackRange[1], 14,14,self.x,self.y)
        draw_rectangle(self.x - self.width/2,self.y - self.height/2,
                       self.x + self.width/2,self.y + self.height/2)

    def move(self):
        ratio = 1
        if self.bslow == True:
            ratio = 0.5
        else:
            ratio = 1

        self.x += self.velocity[0] * MainFrameWork.frame_time * ratio
        self.y += self.velocity[1] * MainFrameWork.frame_time * ratio

def Init_Bullet(Bullet):

    Bullet.rot = 90
    Bullet.dmg = 1

    bSPEED_KMPH = 100.0  # 100 km/h

    radian_rot = math.radians(Bullet.rot)

    cos = math.cos(radian_rot)
    sin = math.sin(radian_rot)

    Bullet.velocity[0] = cos * bSPEED_KMPH
    Bullet.velocity[1] = sin * bSPEED_KMPH
