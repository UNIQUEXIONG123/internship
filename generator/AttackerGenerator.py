from typing import Set
from attacker.Attacker import Attacker
from generator import AttackerMode
from generator.DefenderGenerator import defender_generator_proxy, DefenderGeneratorProxy
from generator.EnvironmentEntity import attacker_mode_list


class AttackerGenerator:

    # 这里新传入一个list，里面储存的是数字，依据AttackerMode中的字典判断是哪种攻击模式，在攻击模式类中进行生成
    def __init__(self, p_attacker_mode_list, p_defender_generator_proxy: DefenderGeneratorProxy):
        # attacker_mode_list储存了顺序的攻击模式，循环访问每一个模式进行生成
        self.attacker_mode_list = p_attacker_mode_list

        # 定义范型集合
        generic_set = Set[Attacker]

        # 创建attacker集合，生产一个就放进去一个
        self.attacker_set: generic_set = set()
        self.defender_generator_proxy = p_defender_generator_proxy

    def generate(self):
        """
        生成场景，生成的所有attacker实体将会放在set当中，同时通知defender将新的进攻实体放在队列中
        :return:
        """
        for mode in self.attacker_mode_list:
            generator = AttackerMode.attacker_mode_dic[mode]()
            attackers = generator.generate()
            if isinstance(attackers, tuple):  # 判断返回值是否是元组
                for attacker in attackers:
                    if isinstance(attacker, Attacker):
                        if attacker.get_is_alive():   # 增加这个判定是如果导弹射不中，就不要加入准备队列
                            self.notify(attacker)
                        else:
                            # TODO: 如果发现有输出a dead attacker, 代表数据生成不合理，敌方打不到我方
                            print("a dead attacker: ", attacker.get_type(), attacker.get_mode_name())
            else:
                self.notify(attackers)

    def notify(self, attacker_entity):
        """
        当生产出来一个敌方目标，就将这个敌方目标放到prepared_list当中, 通过代理实现
        :param attacker_entity:
        :return:
        """
        self.defender_generator_proxy.notified(attacker_entity)

    # 挡attacker被拦截，该attacker将会通知factory我被击毁，该attacker将被从set移除，同时将defender对应的对象移除
    def destroy_notify(self, attacker_entity):
        pass


attacker_generator = AttackerGenerator(attacker_mode_list, defender_generator_proxy)
