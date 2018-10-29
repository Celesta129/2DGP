from pico2d import *
from FrameWork.CObject import cObject
from FrameWork.CBullet import *

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


class IdleState:
    @staticmethod
    def enter(Player,event):
        Player.ObjectInfo.image_bottom = cPlayer.Player_image.h - 32 - int(Player.ObjectInfo.image_height * 0.5)
        pass

    @staticmethod
    def exit(Player,event):
        pass

    @staticmethod
    def do(Player,_bullet_list):
        Player.ObjectInfo.frame = (Player.ObjectInfo.frame +1) % 4
        Player.ObjectInfo.y += Player.ObjectInfo.velocity[1]

        if (Player.shot_timer <= 0):
            if Player.shot == True:
                Bullet = cBullet(Player.ObjectInfo.x, Player.ObjectInfo.y, "P2", PLAYER1)
                Init_Bullet(Bullet)
                _bullet_list.insert(0, Bullet)
            Player.shot_timer = Player.shot_timer_max
        else:
            Player.shot_timer -= 0.05

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
        if event == X_DOWN:
            Player.shot()
        pass

    @staticmethod
    def do(Player,_bullet_list):
        Player.ObjectInfo.frame = (Player.ObjectInfo.frame + 1) % 7
        Player.ObjectInfo.x += Player.ObjectInfo.velocity[0]
        Player.ObjectInfo.y += Player.ObjectInfo.velocity[1]

        if(Player.shot_timer <= 0):
            if Player.shot == True:
                Bullet = cBullet(Player.ObjectInfo.x, Player.ObjectInfo.y, "P2", PLAYER1)
                Init_Bullet(Bullet)
                _bullet_list.insert(0, Bullet)
            Player.shot_timer = Player.shot_timer_max
        else:
            Player.shot_timer -=0.05

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
                NONE: IdleState
                },

    MoveState: {RIGHT_UP : MoveState, LEFT_UP: MoveState,
                UP_UP : IdleState, DOWN_UP : IdleState,
                RIGHT_DOWN: MoveState, LEFT_DOWN: MoveState,
                UP_DOWN: MoveState, DOWN_DOWN: MoveState,
                X_DOWN: MoveState, X_UP: MoveState,
                NONE: IdleState
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

        self.shot = False
        self.shot_timer_max = 0.5
        self.shot_timer = 0.5

    def add_event(self, event):
        self.event_que.insert(0,event)

    def update(self, _bullet_list):
        self.cur_state.do(self,_bullet_list)
        if len(self.event_que) > 0 :
            event = self.event_que.pop()
            self.cur_state.exit(self,event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self,event)

        if (self.ObjectInfo.velocity[0] > 0):
            self.ObjectInfo.flip = True
        else:
            self.ObjectInfo.flip = False
        pass

    def shot(self,_bullet_list):
        print('Shot')

        pass
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

            self.add_event(key_event)


        pass

    def draw(self):
        self.ObjectInfo.draw()