from FrameWork import Game_World
from FrameWork.Class.Enemy.EnemyClass.Enemy_Zaco_Blue import Zaco_Blue
from FrameWork.Class.Enemy.EnemyClass.Enemy_Zaco_Red import Zaco_Red

from FrameWork.Game_World import *
name = "Enemy_Generator"

def read_file(stage_number,final_object_info):
    filename = None
    if stage_number == 0:
        filename = "Stage_01.txt"
    elif stage_number == 1:
        filename = "Stage_02.txt"
    else:
        return
    with open(filename, "r") as f:
        lines = f.readlines()
        # 한줄을 읽는다.
        for line in lines:
            array = ""
            # 구분자 단위로 숫자를 읽어들인다.
            for character in line:
                if character == "|":
                    read_array_to_float(array, final_object_info)
                    array = ""
                else:
                    array += character

            pass

# First "|" = Time
# second "|" = Type of enemy
# Third "|" = posX
# fourth "|" = posY

ENEMYTYPE, POSX, POSY = range(3)
ZACO_BLUE,ZACO_RED = range(2)

enemy_table = {ZACO_BLUE : Zaco_Blue,
               ZACO_RED : Zaco_Red}

def read_array_to_float(array, output_array):
    value = float(array)
    output_array.append(value)


 # 최종 정보를 이용해 Enemy 생성
def make_Enemy(info_array, cur_stage_timeacc):
    if len(info_array) == 0 :
        return
    if info_array[0] > cur_stage_timeacc :
        return

    Enemy_type = info_array[1]

    x,y = info_array[2],info_array[3]
    Enemy = enemy_table[Enemy_type](x,y)

    Game_World.add_object(Enemy,Game_World.layer_enemy)
    for i in range(4):
        info_array.pop(0)
    pass