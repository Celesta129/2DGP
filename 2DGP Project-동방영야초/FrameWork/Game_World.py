
# layer 0: Background Objects
#list_objects = 1
#list_Bullet_playerTenemy = 2
#list_Bullet_enemyTplayer = 3

layer_object, layer_pTe, layer_eTp, layer_end = range(4)
objects = [[],[],[],[]]

def add_object(object, layer):
    objects[layer].append(object)


def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o


def clear():
    for o in all_objects():
        del o
    objects.clear()


def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o

