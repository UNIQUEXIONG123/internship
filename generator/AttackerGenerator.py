from typing import Set
from attacker.Attacker import Attacker
from generator import AttackerMode


class AttackerGenerator:

    # 这里新传入一个list，里面储存的是数字，依据AttackerMode中的字典判断是哪种攻击模式，在攻击模式类中进行生成
    def __init__(self, attacker_mode_list):
        # attacker_mode_list储存了顺序的攻击模式，循环访问每一个模式进行生成
        self.attacker_mode_list = attacker_mode_list

        # 定义范型集合
        generic_set = Set[Attacker]

        # 创建attacker集合，生产一个就放进去一个
        self.attacker_set: generic_set = set()

    # 生成场景，生成的所有attacker实体将会放在set当中，同时通知defender将新的进攻实体放在队列中
    def generate(self):
        for mode in self.attacker_mode_list:
            generator = AttackerMode.AttackerModeDic[mode]()
            generator.generate()

    # 当生产出来一个敌方目标，就将这个敌方目标放到prepared_list当中
    def notify(self, attacker_entity):
        pass

    # 挡attacker被拦截，该attacker将会通知factory我被击毁，该attacker将被从set移除，同时将defender对应的对象移除
    def destroy_notify(self, attacker_entity):
        pass
