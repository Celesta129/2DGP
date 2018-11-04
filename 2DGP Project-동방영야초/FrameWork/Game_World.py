
# layer 0: Background Objects
# Layer 1 : foreground Objects

layer_background, layer_player, layer_enemy = range(3)
layer_pTe, layer_eTp = range(2)
objects = [[],[],[]]
bullets = [[],[]]


def add_object(object, layer):
    objects[layer].append(object)


def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break

def clear():
    for o in all_objects():
        del o
    objects.clear()


def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o


def add_bullet(bullet, layer):
    bullets[layer].append(bullet)


def remove_bullet(o):
    for i in range(len(bullets)):
        if o in bullets[i]:
            bullets[i].remove(o)
            del o
            break


def clear_bullet():
    for o in all_bullets():
        del o
    bullets.clear()


def all_bullets():
    for i in range(len(bullets)):
        for o in bullets[i]:
            yield o