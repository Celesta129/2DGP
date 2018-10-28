from pico2d import *
from FrameWork.CObject import cObject
from FrameWork.CBullet import *

RIGHT_DOWN, LEFT_DOWN, UP_DOWN, DOWN_DOWN, RIGHT_UP, LEFT_UP, UP_UP, DOWN_UP, X_DOWN, X_UP  = range(10)
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




class IdleState:
    @staticmethod
    def enter(Player):
        Player.ObjectInfo.image_bottom = cPlayer.Player_image.h - 32 - int(Player.ObjectInfo.image_height * 0.5)
        pass

    @staticmethod
    def exit(Player):
        pass

    @staticmethod
    def do(Player,_bullet_list):
        Player.ObjectInfo.frame = (Player.ObjectInfo.frame +1) % 4
        Player.ObjectInfo.y += Player.ObjectInfo.velocity[1]

        if Player.shot == True:
            Bullet = cBullet(Player.ObjectInfo.x, Player.ObjectInfo.y, "P", ZACO1)
            _bullet_list.insert(0, Bullet)
    @staticmethod
    def draw(Player):
        Player.draw()

class MoveState:
    @staticmethod
    def enter(Player):
        Player.ObjectInfo.image_bottom = cPlayer.Player_image.h - 82 - int(Player.ObjectInfo.image_height*0.5)
        pass

    @staticmethod
    def exit(Player):
        pass

    @staticmethod
    def do(Player,_bullet_list):
        Player.ObjectInfo.frame = (Player.ObjectInfo.frame + 1) % 7
        Player.ObjectInfo.x += Player.ObjectInfo.velocity[0]
        Player.ObjectInfo.y += Player.ObjectInfo.velocity[1]

        if Player.shot == True:
            Bullet = cBullet(Player.ObjectInfo.x, Player.ObjectInfo.y, "P", ZACO2)
            _bullet_list.insert(0, Bullet)
    @staticmethod
    def draw(Player):
        Player.draw()

next_state_table = {
# fill here
    IdleState: {RIGHT_UP : MoveState, LEFT_UP: MoveState,
                UP_UP : MoveState, DOWN_UP : MoveState,
                RIGHT_DOWN: MoveState, LEFT_DOWN: MoveState,
                UP_DOWN: MoveState, DOWN_DOWN: MoveState,
                X_DOWN: IdleState, X_UP: IdleState
                },

    MoveState: {RIGHT_UP : MoveState, LEFT_UP: MoveState,
                UP_UP : MoveState, DOWN_UP : MoveState,
                RIGHT_DOWN: MoveState, LEFT_DOWN: MoveState,
                UP_DOWN: MoveState, DOWN_DOWN: MoveState,
                X_DOWN: MoveState, X_UP: MoveState
                }
}

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
        self.ObjectInfo.frame_offset = 32

        self.event_que = []
        self.cur_state = IdleState

        self.shot = False

    def add_event(self, event):
        self.event_que.insert(0,event)

    def update(self, _bullet_list):
        self.cur_state.do(self,_bullet_list)
        if len(self.event_que) > 0 :
            event = self.event_que.pop()
            self.change_state(next_state_table[self.cur_state][event])
        pass

    def change_state(self,state):
        self.cur_state.exit(self)
        self.cur_state = state
        self.cur_state.enter(self)

    def handle_event(self,event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if key_event == RIGHT_DOWN:
                self.ObjectInfo.velocity[0] += 1
            elif key_event == LEFT_DOWN:
                self.ObjectInfo.velocity[0] -= 1
            elif key_event == UP_DOWN:
                self.ObjectInfo.velocity[1] += 1
            elif key_event == DOWN_DOWN:
                self.ObjectInfo.velocity[1] -= 1
            elif key_event == RIGHT_UP:
                self.ObjectInfo.velocity[0] -= 1
            elif key_event == LEFT_UP:
                self.ObjectInfo.velocity[0] += 1
            elif key_event == UP_UP:
                self.ObjectInfo.velocity[1] -= 1
            elif key_event == DOWN_UP:
                self.ObjectInfo.velocity[1] += 1

            if(self.ObjectInfo.velocity[0] >= 1 ):
                self.ObjectInfo.flip = True
            else:
                self.ObjectInfo.flip = False

            self.add_event(key_event)

            if(key_event == X_DOWN):
                self.shot = True
            elif key_event == X_UP:
                self.shot = False
        pass

    def draw(self):
        self.ObjectInfo.draw()