from FrameWork import Game_World
from FrameWork.Class.Enemy.EnemyClass.Enemy_Zaco_Blue import Zaco_Blue
from FrameWork.Class.Enemy.EnemyClass.Enemy_Zaco_Red import Zaco_Red
import json
from FrameWork.Game_World import *
name = "Enemy_Generator"

def read_file(stage_number):

    filename = None
    if stage_number == 0:
        filename = "Stage_01.json"
    elif stage_number == 1:
        filename = "Stage_02.json"
    else:
        return
    with open(filename, "r") as f:
        final_object_info = json.load(f)

    return final_object_info


# First "|" = Time
# second "|" = Type of enemy
# Third "|" = posX
# fourth "|" = posY

ENEMYTYPE, POSX, POSY = range(3)

enemy_table = {"ZACO_BLUE" : Zaco_Blue,
               "ZACO_RED" : Zaco_Red}

def load_dic_by_json(file):
    array = json.load(file)
    return array

def read_array_to_float(array, output_array):
    value = float(array)
    output_array.append(value)


 # 최종 정보를 이용해 Enemy 생성
def make_Enemy(info_array, cur_stage_timeacc):
    if len(info_array) == 0 :
        return
    if info_array[0]["Time"] > cur_stage_timeacc :
        return

    Enemy_type = info_array[0]["Type"]

    x,y = info_array[0]["x"], info_array[0]["y"]
    Enemy = enemy_table[Enemy_type](x,y)

    Game_World.add_object(Enemy,Game_World.layer_enemy)
    info_array.pop(0)
    pass