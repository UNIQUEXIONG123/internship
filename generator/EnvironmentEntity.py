import random

from generator.AttackerGenerator import AttackerGenerator
from generator.DefenderGenerator import DefenderGenerator


# 生成一些生成场景的初始数据
def init():
    mode_num = random.randint(1, 10)
    mode_list = []
    for num in range(mode_num):
        mode_list.append(random.randint(1, 9))
    return mode_list


attacker_mode_list = init()
attacker_generator = AttackerGenerator(attacker_mode_list)
defender_generator = DefenderGenerator(24, 120, 200, 400)


class Client:
    def __init__(self, attacker_generator_client, defender_generator_client):
        self.attacker_generator = attacker_generator_client
        self.defender_generator = defender_generator_client


client = Client(attacker_generator, defender_generator)
