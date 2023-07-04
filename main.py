from generator.AttackerGenerator import AttackerGenerator
from generator.DefenderGenerator import DefenderGenerator
import generator.AttackerMode as am


# 生成一些生成场景的初始数据
def init():
    # 生成场景的模式
    mode_map = {
        "MODE_1": 2,
        "MODE_2": 3,
        "MODE_3": 5,
        "MODE_4": 7,
        "MODE_5": 11,
        "MODE_6": 13,
        "MODE_7": 17,
        "MODE_8": 19,
        "MODE_9": 23
    }
    return mode_map


if __name__ == '__main__':
    generator_mode_map = init()
    attacker_mode_list = [1, 2, 3, 4, 5, 6, 7, 6, 3, 5]
    attacker_generator = AttackerGenerator(attacker_mode_list)
    attacker_generator.generate()
    # defender_generator = DefenderGenerator()
