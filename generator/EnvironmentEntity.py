import random


# 生成一些生成场景的初始数据
def init():
    mode_num = random.randint(1, 10)
    mode_list = []
    for num in range(mode_num):
        mode_list.append(random.randint(1, 9))
    return mode_list


attacker_mode_list = init()
