from pico2d import *

<<<<<<< HEAD

def handle_events():
    # fill here
    pass


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
frame = 0

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, 90)
=======
def handle_events():
    # fill here
    global running
    global x,y
    global cursorX, cursorY
    global nextPosX,nextPosY
    global dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            nextPosX, nextPosY, = event.x, KPU_HEIGHT - 1 - event.y
            if x < nextPosX:
                dir = 1
            elif x > nextPosX:
                dir = 0

        elif event.type == SDL_MOUSEMOTION:
            cursorX, cursorY =  event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                running = False


def run_charactor():
    global x,y
    global nextPosX, nextPosY
    global dir

    if x > nextPosX:
        x -= 1
    elif x < nextPosX:
        x += 1
    if nextPosY > y:
       y +=1
    elif nextPosY < y:
        y -=1

    if x == nextPosX and x == nextPosY:
        if dir == 0:
            dir = 2
        elif dir== 1:
            dir = 4
    pass

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')
running = True

x,y = KPU_WIDTH//2, KPU_HEIGHT//2
nextPosX, nextPosY =  KPU_WIDTH//2, KPU_HEIGHT//2


cursorX = 0
cursorY = 0
frame = 0
dir = 1
#왼쪽 0 오른쪽 1

hide_cursor()
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH//2, KPU_HEIGHT//2)
    character.clip_draw(frame * 100, 100 * dir, 100, 100, x, y)

    hand_arrow.draw(cursorX,cursorY)
>>>>>>> 6d4636b6ca683ec7c8603e3a7e8a802ab52e10ca
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8

<<<<<<< HEAD
    delay(0.05)
=======
    run_charactor()
    delay(0.02)
>>>>>>> 6d4636b6ca683ec7c8603e3a7e8a802ab52e10ca

close_canvas()

