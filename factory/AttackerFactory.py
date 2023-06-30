from typing import Set

from attacker.Attacker import Attacker


class AttackerFactory:

    # 攻击方的进攻模式，大概15种，先写9种
    class AttackerMode:
        MODE_1 = 1
        MODE_2 = 2
        MODE_3 = 3
        MODE_4 = 4
        MODE_5 = 5
        MODE_6 = 6
        MODE_7 = 7
        MODE_8 = 8
        MODE_9 = 9

    def __init__(self, attacker_mode):
        self.attacker_mode = attacker_mode

        # 定义范型集合
        generic_set = Set[Attacker]

        # 创建attacker集合，生产一个就放进去一个
        self.attacker_set: generic_set = set()

    # 生成场景，生成的所有attacker实体将会放在set当中，同时通知defender将新的进攻实体放在队列中
    def generate(self):
        if self.attacker_mode == AttackerFactory.AttackerMode.MODE_1:
            pass
        elif self.attacker_mode == AttackerFactory.AttackerMode.MODE_2:
            pass
        elif self.attacker_mode == AttackerFactory.AttackerMode.MODE_3:
            pass
        elif self.attacker_mode == AttackerFactory.AttackerMode.MODE_4:
            pass
        elif self.attacker_mode == AttackerFactory.AttackerMode.MODE_5:
            pass
        elif self.attacker_mode == AttackerFactory.AttackerMode.MODE_6:
            pass
        elif self.attacker_mode == AttackerFactory.AttackerMode.MODE_7:
            pass
        elif self.attacker_mode == AttackerFactory.AttackerMode.MODE_8:
            pass
        elif self.attacker_mode == AttackerFactory.AttackerMode.MODE_9:
            pass
        else:
            pass

    # 挡attacker被拦截，该attacker将会通知factory我被击毁，该attacker将被从set移除，同时将defender对应的对象移除
    def destroy_notify(self, attacker_entity):
        pass
