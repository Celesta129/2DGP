from pico2d import *
from FrameWork import CObject
from FrameWork import MainFrameWork

from FrameWork.CBullet import *
from FrameWork import Game_World

# Player Events
RIGHT_DOWN, LEFT_DOWN, UP_DOWN, DOWN_DOWN, RIGHT_UP, LEFT_UP, UP_UP, DOWN_UP, X_DOWN, X_UP, NONE  = range(11)
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYDOWN, SDLK_x) : X_DOWN,
    (SDL_KEYUP, SDLK_x): X_UP,
}
sprite_offset_x = 32
sprite_offset_y = 50


SPEED_KMPH = 60.0          # 60 km/h
SPEED_MPM = SPEED_KMPH * 1000.0 / 60.0
SPEED_MPS = SPEED_MPM / 60.0
SPEED_PPS = SPEED_MPS * CObject.PIXEL_PER_METER # Pixel Per second

class IdleState:
    @staticmethod
    def enter(Player,event):
        Player.ObjectInfo.image_bottom = cPlayer.Player_image.h - 32 - int(Player.ObjectInfo.image_height * 0.5)
        pass

    @staticmethod
    def exit(Player,event):

        pass

    @staticmethod
    def do(Player):
        Player.ObjectInfo.frame = (Player.ObjectInfo.frame +1) % 4
        Player.move()


    @staticmethod
    def draw(Player):
        Player.draw()

class MoveState:
    @staticmethod
    def enter(Player,event):
        Player.ObjectInfo.image_bottom = cPlayer.Player_image.h - 82 - int(Player.ObjectInfo.image_height*0.5)
        pass

    @staticmethod
    def exit(Player,event):

        pass

    @staticmethod
    def do(Player):
        Player.ObjectInfo.frame = (Player.ObjectInfo.frame + 1) % 7
        Player.move()

    @staticmethod
    def draw(Player):
        Player.draw()

next_state_table = {
# fill here
    IdleState: {RIGHT_UP : MoveState, LEFT_UP: MoveState,
                UP_UP : MoveState, DOWN_UP : MoveState,
                RIGHT_DOWN: MoveState, LEFT_DOWN: MoveState,
                UP_DOWN: MoveState, DOWN_DOWN: MoveState,
                X_DOWN: IdleState, X_UP: IdleState,

                },

    MoveState: {RIGHT_UP : MoveState, LEFT_UP: MoveState,
                UP_UP : MoveState, DOWN_UP : MoveState,
                RIGHT_DOWN: MoveState, LEFT_DOWN: MoveState,
                UP_DOWN: MoveState, DOWN_DOWN: MoveState,
                X_DOWN: MoveState, X_UP: MoveState,
                }
}

def Init_Bullet(Bullet):
    Bullet.ObjectInfo.velocity[1] = 2
    Bullet.ObjectInfo.rot = 90
    Bullet.dmg = 1


name = "class_Player"
class cPlayer:
    Player_image = None
    def __init__(self,x,y):
        self.ObjectInfo = cObject()
        if cPlayer.Player_image == None:
            cPlayer.Player_image = load_image("Players.png")
        self.ObjectInfo.x = x
        self.ObjectInfo.y = y
        self.ObjectInfo.image = cPlayer.Player_image
        self.ObjectInfo.image_width = 24
        self.ObjectInfo.image_height = 42

        self.ObjectInfo.width = 24
        self.ObjectInfo.height = 42

        self.ObjectInfo.image_left = 28 - (int)(self.ObjectInfo.image_width*0.5)
        self.ObjectInfo.image_bottom = cPlayer.Player_image.h - 32 - int(self.ObjectInfo.image_height*0.5)
        self.ObjectInfo.frame_offset = sprite_offset_x

        self.event_que = []
        self.cur_state = IdleState

        self.bshot = False
        self.shot_timer_max = 0.5
        self.shot_timer = 0.5

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

        if (self.ObjectInfo.velocity[0] > 0):
            self.ObjectInfo.flip = True
        elif self.ObjectInfo.velocity[0] == 0:
            self.cur_state = IdleState
            self.ObjectInfo.image_bottom = cPlayer.Player_image.h - 32 - int(self.ObjectInfo.image_height * 0.5)
        else:
            self.ObjectInfo.flip = False

        self.shot()
        pass

    def shot(self):
        if self.bshot == True:
            if (self.shot_timer <= 0):
                Bullet = cBullet(self.ObjectInfo.x, self.ObjectInfo.y, "P2", PLAYER1)
                Init_Bullet(Bullet)
                Game_World.add_bullet(Bullet,1)
                self.shot_timer = self.shot_timer_max
                print('Shot')
            else:
                self.shot_timer -= 0.05


    def handle_event(self,event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if key_event == RIGHT_DOWN:
                self.ObjectInfo.velocity[0] += SPEED_PPS
            elif key_event == LEFT_DOWN:
                self.ObjectInfo.velocity[0] -= SPEED_PPS
            elif key_event == UP_DOWN:
                self.ObjectInfo.velocity[1] += SPEED_PPS
            elif key_event == DOWN_DOWN:
                self.ObjectInfo.velocity[1] -= SPEED_PPS
            elif key_event == RIGHT_UP:
                self.ObjectInfo.velocity[0] -= SPEED_PPS
            elif key_event == LEFT_UP:
                self.ObjectInfo.velocity[0] += SPEED_PPS
            elif key_event == UP_UP:
                self.ObjectInfo.velocity[1] -= SPEED_PPS
            elif key_event == DOWN_UP:
                self.ObjectInfo.velocity[1] += SPEED_PPS
            elif key_event == X_DOWN:
                self.bshot = True
            elif key_event == X_UP:
                self.bshot = False

            self.add_event(key_event)


        pass

    def draw(self):
        self.ObjectInfo.draw()

    def move(self):
        self.ObjectInfo.x += self.ObjectInfo.velocity[0] * MainFrameWork.frame_time
        self.ObjectInfo.y += self.ObjectInfo.velocity[1] * MainFrameWork.frame_time
