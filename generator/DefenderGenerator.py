import random
from typing import List

from attacker.Attacker import Attacker
from defender.MC import MC
from defender.MRAD import MRAD
from defender.SCNG import SCNG
from defender.SRAD import SRAD


class DefenderGenerator:
    """
    这里的工厂相当于某一艘舰船
    导弹有初速度并且保持不变，同时施加延迟
    舰炮有初速度，同时施加角速度的影响
    """

    def __init__(self, mrad_animation, srad_animation, scng_animation, mc_animation):
        # 准备队列
        self.prepare_list: List[Attacker] = []
        # 分配队列
        self.allocate_list: List[Attacker] = []
        # 发射队列
        self.launch_list: List[Attacker] = []
        # 记录弹药量
        self.animation_map = {
            "mrad_animation": mrad_animation,
            "srad_animation": srad_animation,
            "scng_animation": scng_animation,
            "mc_animation": mc_animation
        }

    def get_prepare_list(self) -> List[Attacker]:
        return self.prepare_list

    def add_prepare_list(self, attacker: Attacker):
        self.prepare_list.append(attacker)

    def notified(self, attacker):
        """
        在代理中被调用，每生产出来一个实体就加入prepared_list中
        :param attacker:
        :return:
        """
        self.prepare_list.append(attacker)

    def generate(self):
        """
        生成防御器材
        其中speed：m/s
            delay: s
            angular_velocity:rad/s
        """
        # TODO:车载导弹也需要考虑转动的时间，多次打击情况下的导弹车不需要转向，决定因素是填充时间

        # 生成MRAD
        for _ in range(self.animation_map["mrad_animation"]):
            speed = random.gauss(1000, 50)  # 使用高斯分布生成速度
            delay = random.gauss(0.8, 0.02)  # 使用高斯分布生成延迟
            mrad = MRAD(speed, delay)  # 创建MRAD对象
            self.allocate_list.append(mrad)  # 将MRAD对象添加到分配队列中

        # 生成SRAD
        for _ in range(self.animation_map["srad_animation"]):
            speed = random.gauss(800, 20)  # 使用高斯分布生成速度
            delay = random.gauss(0.8, 0.02)  # 使用高斯分布生成延迟

            srad = SRAD(speed, delay)  # 创建SRAD对象
            self.allocate_list.append(srad)  # 将SRAD对象添加到分配队列中

        # 生成SCNG
        for _ in range(self.animation_map["scng_animation"]):
            speed = random.gauss(500, 10)  # 使用高斯分布生成速度
            angular_velocity = random.gauss(0.4, 0.01)  # 使用高斯分布生成角速度
            delay = random.gauss(0.8, 0.02)
            scng = SCNG(speed, delay, angular_velocity)  # 创建SCNG对象
            self.allocate_list.append(scng)  # 将SCNG对象添加到分配队列中

        for _ in range(self.animation_map["mc_animation"]):
            speed = random.gauss(800, 20)
            angular_velocity = random.gauss(0.4, 0.01)
            delay = random.gauss(0.8, 0.02)
            mc = MC(speed, delay, angular_velocity)
            self.allocate_list.append(mc)

    def allocate_defenders(self):
        """
        将防御器材从分配队列移到发射队列
        """
        self.launch_list.extend(self.allocate_list)  # 将分配队列中的防御器材添加到发射队列中
        self.allocate_list = []  # 清空分配队列

    def print_list(self):
        """
        打印出分配列表
        :return:
        """
        for defender in self.launch_list:
            print(defender.__class__)

    def print_defenders(self):
        """
        打印发射队列中的防御器材信息
        """
        for defender in self.launch_list:
            if isinstance(defender, MC):
                print("MC:speed: " + str(defender.get_speed()) + ", delay: " + str(defender.get_delay()) +
                      ", angular_velocity: " + str(defender.get_angular_velocity()))
            elif isinstance(defender, SCNG):
                print("SCNG:speed: " + str(defender.get_speed()) + ", delay: " + str(defender.get_delay()) +
                      ", angular_velocity: " + str(defender.get_angular_velocity()))


class DefenderGeneratorProxy:
    def __init__(self, p_defender_generator: DefenderGenerator):
        self.defender_generator = p_defender_generator

    def notified(self, attacker):
        self.defender_generator.notified(attacker)


defender_generator = DefenderGenerator(24, 120, 200, 400)
defender_generator_proxy = DefenderGeneratorProxy(defender_generator)

# # 使用示例
# mrad_animation = 10
# srad_animation = 15
# scng_animation = 30
# mc_animation = 20
#
# factory = DefenderGenerator(mrad_animation, srad_animation, scng_animation, mc_animation)
# factory.generate()
# factory.allocate_defenders()
# factory.print_list()
# factory.print_defenders()
