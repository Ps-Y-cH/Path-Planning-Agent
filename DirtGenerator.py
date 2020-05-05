"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""

import random

def dirt_gen(p):
    list_ = random.sample(range(1, 101), p)
    return list_

def list_to_xy_coord(list_):
    dirtTuples = []
    for x in list_:
        if x % 10 == 0:
            dirtTuples.append([x // 10 - 1, 9])
        else:
            dirtTuples.append([x // 10, x % 10 - 1])
    return dirtTuples
