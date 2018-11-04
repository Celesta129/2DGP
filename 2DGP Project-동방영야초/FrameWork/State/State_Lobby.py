from pico2d import *
from FrameWork import MainFrameWork
from FrameWork.State import State_Stage

image_Lobby = None

Logo_left = 1092
Logo_bottom = 998
Logo_width,Logo_height = 220,380
name = "State_Lobby"



x, y = range(2)
left, bottom, width, height = range(4)
START, QUIT , BUTTON_END = range(3)
# left, bottom, width, height
button_info = {START: (36,673,75,30),
               QUIT: (424,835,57,30) }
button_pos = {START : (160,250),
               QUIT : (130,200)}

button_offset_y = 65

button_select = START
def enter():
    global image_Lobby

    if (image_Lobby == None):
        image_Lobby = load_image("Menu.png")


def exit():
    global image_Lobby
    del(image_Lobby)



def pause():
    pass


def resume():
    pass


def handle_events():
    global button_select
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            MainFrameWork.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            MainFrameWork.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            button_select = (button_select - 1) % BUTTON_END
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            button_select = (button_select + 1) % BUTTON_END
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_z or event.key == SDLK_RETURN:
                if button_select == 0:
                    MainFrameWork.change_state(State_Stage)
                elif button_select == 1:
                    MainFrameWork.quit()
    pass


def update():
    pass


def draw():
    global image_Lobby
    clear_canvas()

    draw_background()

    update_canvas()


def draw_background():
    if image_Lobby != None:
        image_Lobby.clip_draw(14, image_Lobby.h - 529, 640, 480, 400, 300, 800, 600)
        image_Lobby.clip_draw(Logo_left,image_Lobby.h - Logo_bottom, Logo_width, Logo_height, 650,325, Logo_width, 450)
        for i in range(BUTTON_END):
            Left = button_info[i][left]
            Bottom = image_Lobby.h - button_info[i][bottom]
            Width = button_info[i][width]
            Height = button_info[i][height]
            Pos = button_pos[i]
            if i == button_select:
                Bottom += button_offset_y
            image_Lobby.clip_draw(Left, Bottom, Width, Height, Pos[x], Pos[y])
