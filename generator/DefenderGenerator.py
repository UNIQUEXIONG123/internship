import random
from typing import List, Tuple

from attacker.Attacker import Attacker
from defender.Defender import Defender
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
        # 分配队列，用于分配防御武器
        self.allocate_list: List[Defender] = []
        # # 发射队列
        # self.launch_list: List[Attacker] = []
        # # 预计拦截时间
        # self.estimate_list: List[int] = []

        # 把发射弹药和预计拦截时间改成pair python中使用元组存放
        self.destroy_list: List[Tuple[Attacker,int]] = []
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

    def get_allocate_list(self) -> List[Defender]:
        return self.allocate_list

    # def get_launch_list(self) -> List[Attacker]:
    #     return self.launch_list
    # def add_launch_list(self,attacker: Attacker):
    #     self.launch_list.append(attacker)
    #
    # def get_estimate_list(self) -> List[int]:
    #     return self.estimate_list
    # def add_estimate_list(self,estimate_time: int):
    #     self.estimate_list.append(estimate_time)
    #     self.estimate_list.sort()

    def get_destroy_list(self) -> List[Tuple[Attacker, int]]:
        return self.destroy_list
    def add_destroy_list(self, attacker: Attacker, interception_time: int):
        pair = (attacker, interception_time)
        self.destroy_list.append(pair)
        self.destroy_list.sort(key=lambda x: x[1])



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
            由于没有找到角度速度的值，所以根据一般的角速度4rad/s，考虑炮管的长度认为10°/s可能是比较可行？

        """
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
            angular_velocity = random.gauss(10, 1)  # 使用高斯分布生成角速度
            delay = random.gauss(0.8, 0.02)
            direction = 0
            scng = SCNG(speed, delay, angular_velocity,direction)  # 创建SCNG对象
            self.allocate_list.append(scng)  # 将SCNG对象添加到分配队列中
        # 生成MC
        for _ in range(self.animation_map["mc_animation"]):
            speed = random.gauss(800, 20)
            angular_velocity = random.gauss(10, 1)
            delay = random.gauss(0.8, 0.02)
            direction = 0
            mc = MC(speed, delay, angular_velocity,direction)
            self.allocate_list.append(mc)

        self.allocate_list.sort(key=lambda item:item.get_speed())

    def launch_defenders(self,attacker:Attacker,now_time:int):
        """
        将防御器材进行分配发射的时间
        需要返回一个所需时间
        return:time
        """
        print("now prepare launch defender for "+str(attacker.get_type())+" the distance is "+str(attacker.get_distance(now_time)))
        now_defender = self.allocate_list.pop()
        print("the defender is "+str(now_defender.get_type())+" speed is "+ str(now_defender.get_speed()))
        dur_time = 0
        if isinstance(now_defender,MRAD):
            dur_time =  now_defender.get_delay()
            self.animation_map["mrad_animation"] -= 1
        elif isinstance(now_defender,SRAD):
            dur_time = now_defender.get_delay()
            self.animation_map["srad_animation"] -= 1
        elif isinstance(now_defender,MC) :
            defend_direction = now_defender.get_direction()
            attacker_direction = attacker.get_direction(now_time)
            abs_direction = abs(defend_direction-attacker_direction)
            for item in self.allocate_list:
                if isinstance(item,MC):
                    item.set_direction(attacker_direction)
            now_defender.set_direction(attacker_direction)
            if abs_direction > 180:
                abs_direction = 360-abs_direction
            time = abs_direction / now_defender.get_angular_velocity()
            self.animation_map["mc_animation"]-=1
            dur_time = max(time,now_defender.get_delay())

        elif isinstance(now_defender,SCNG):
            defend_direction = now_defender.get_direction()
            attacker_direction = attacker.get_direction(now_time)
            abs_direction = abs(defend_direction - attacker_direction)
            for item in self.allocate_list:
                if isinstance(item, SCNG):
                    item.set_direction(attacker_direction)
            now_defender.set_direction(attacker_direction)
            if abs_direction > 180:
                abs_direction = 360-abs_direction
            time = abs_direction / now_defender.get_angular_velocity()
            self.animation_map["scng_animation"] -= 1
            dur_time = max(time, now_defender.get_delay())


        except_time = 0
        # !TODO 预期时间
        return dur_time,except_time
    # def get_except_time(self):

    # def print_launch(self):
    #     """
    #     打印出发射队列中的器材信息
    #     :return:
    #     """
    #     for defender in self.launch_list:
    #         if isinstance(defender, MC):
    #             print("MC:speed: " + str(defender.get_speed()) + ", delay: " + str(defender.get_delay()) +
    #                   ", angular_velocity: " + str(defender.get_angular_velocity()))
    #         elif isinstance(defender, SCNG):
    #             print("SCNG:speed: " + str(defender.get_speed()) + ", delay: " + str(defender.get_delay()) +
    #                   ", angular_velocity: " + str(defender.get_angular_velocity()))
    #         elif isinstance(defender, MRAD):
    #             print("MRAD:speed: " + str(defender.get_speed()) + ", delay: " + str(defender.get_delay()))
    #         elif isinstance(defender, SRAD):
    #             print("SRAD:speed: " + str(defender.get_speed()) + ", delay: " + str(defender.get_delay()))

    def print_allocate(self):
        """
        打印分配队列中的防御器材信息
        """
        for defender in self.allocate_list:
            if isinstance(defender, MC):
                print("MC:speed: " + str(defender.get_speed()) + ", delay: " + str(defender.get_delay()) +
                      ", angular_velocity: " + str(defender.get_angular_velocity()) + ", now_direction: " + str(defender.get_direction()))
            elif isinstance(defender, SCNG):
                print("SCNG:speed: " + str(defender.get_speed()) + ", delay: " + str(defender.get_delay()) +
                      ", angular_velocity: " + str(defender.get_angular_velocity()) + ", now_direction: " + str(defender.get_direction()))
            elif isinstance(defender,MRAD):
                print("MRAD:speed: " + str(defender.get_speed()) + ", delay: " + str(defender.get_delay()))
            elif isinstance(defender,SRAD):
                print("SRAD:speed: " + str(defender.get_speed()) + ", delay: " + str(defender.get_delay()))


class DefenderGeneratorProxy:
    def __init__(self, p_defender_generator: DefenderGenerator):
        self.defender_generator = p_defender_generator

    def notified(self, attacker):
        self.defender_generator.notified(attacker)


defender_generator = DefenderGenerator(20, 50, 200, 40)
defender_generator_proxy = DefenderGeneratorProxy(defender_generator)
defender_generator.generate()
# defender_generator.print_allocate()
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
