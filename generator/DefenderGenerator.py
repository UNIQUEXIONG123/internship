import math
import random
from typing import List, Tuple

import numpy as np
from scipy.optimize import root_scalar
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
        self.destroy_list: List[Tuple[Attacker,int,int]] = []
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
    def add_destroy_list(self, attacker: Attacker, interception_time: int,destory_random: int):
        pair = (attacker, interception_time,destory_random)
        self.destroy_list.append(pair)
        self.destroy_list.sort(key=lambda x: x[1],reverse=True)



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
    # def get_attacker_model(self,attacker:Attacker):
    #     return attacker.get_mode_name()

    def launch_defenders(self,attacker:Attacker,now_time:int):
        """
        将防御器材进行分配发射的时间
        需要返回一个所需时间
        return:time
        """
        # self.prepare_list.pop()
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

        destory_random = calculate_random(attacker,now_defender)
        except_time = 0
        # !TODO 预期时间
        attacker_mode = attacker.get_mode_name()
        print(attacker_mode)
        if "MODE_3" in str(attacker_mode):
            print("平抛飞行模型")
            # v0 = attacker.get_speed(now_time)
            # v1 = now_defender.get_speed()
            # h0 = attacker.get_height(now_time)
            # d0 = attacker.get_distance(now_time)
            # theta0 = attacker.get_direction(now_time) # 攻击武器的角度
            except_time = calculate_encounter_time(attacker, now_defender,now_time)
            # print("相遇时间：", except_time, "秒")
        if "MODE_2" in str(attacker_mode) or "FIGHTER_MODE" in str(attacker_mode) or "HELICOPTER_MODE" in str(attacker_mode):
            print("俯冲飞行模型")
            v0 = attacker.get_speed(now_time)
            v1 = now_defender.get_speed()
            h0 = attacker.get_height(now_time)
            d0 = attacker.get_distance(now_time)
            except_time = math.sqrt((h0**2 + d0**2)/(v0+v1)**2)
            # print("相遇时间：", except_time, "秒")
        if "MODE_1" in str(attacker_mode):
            print("直线飞行模型")
            v0 = attacker.get_speed(now_time)
            v1 = now_defender.get_speed()
            h0 = attacker.get_height(now_time)
            except_time = h0/(v0+v1)
            # print("相遇时间：", except_time, "秒")
        if "BOMBER_MODE" in str(attacker_mode) or "TRANSPORT_MODE" in str(attacker_mode):
            print("高空直线飞行模型")
            v1 = now_defender.get_speed()
            h0 = attacker.get_height(now_time)
            d0 = attacker.get_distance(now_time)
            except_time = math.sqrt(d0**2 + h0**2)/v1
        print("相遇时间：", except_time+now_time, "秒")
        return dur_time,except_time,destory_random
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


defender_generator = DefenderGenerator(8, 10, 20, 15)
defender_generator_proxy = DefenderGeneratorProxy(defender_generator)
defender_generator.generate()


def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def calculate_random(attacker, now_defender):
    # 初始的基准随机值为0.55
    base_random = 0.55
    attacker_mode = attacker.get_mode_name()  # 获取攻击方的模式名称
    defender_mode = now_defender.get_type()   # 获取防御方的类型

    # # 打印攻击方的模式名称和防御方的类型
    # print(attacker_mode)
    # print(defender_mode)

    # 根据防御方类型施加影响
    if "MRAD" in str(defender_mode):
        # 如果防御方类型包含"MRAD"，则在基准随机值上增加一个在[0, 0.25]区间内的随机值
        base_random += random.uniform(0, 0.25)

    if "MC" in str(defender_mode):
        # 如果防御方类型包含"MC"，则在基准随机值上增加一个在[0, 0.15]区间内的随机值
        base_random += random.uniform(0, 0.15)

    if "SCNG" in str(defender_mode):
        # 如果防御方类型包含"SCNG"，则在基准随机值上增加一个在[0, 0.1]区间内的随机值
        base_random += random.uniform(0, 0.1)

    if "SCAD" in str(defender_mode):
        # 如果防御方类型包含"SCAD"，则在基准随机值上增加一个在[0, 0.15]区间内的随机值
        base_random += random.uniform(0, 0.15)

    # 根据攻击方模式施加影响
    if "MODE_1" in str(attacker_mode):
        # 如果攻击方模式包含"MODE_1"，则在基准随机值上减去一个在[0, 0.05]区间内的随机值
        base_random -= random.uniform(0, 0.05)

    if "MODE_2" in str(attacker_mode):
        # 如果攻击方模式包含"MODE_2"，则在基准随机值上减去0.15
        base_random -= 0.15

    if "MODE_3" in str(attacker_mode):
        # 如果攻击方模式包含"MODE_3"，则在基准随机值上减去一个在[0, 0.05]区间内的随机值
        base_random -= random.uniform(0, 0.05)

    if "BOMBER_MODE" in str(attacker_mode):
        # 如果攻击方模式包含"BOMBER_MODE"，则在基准随机值上减去一个在[0, 0.15]区间内的随机值
        base_random -= random.uniform(0, 0.15)

    if "TRANSPORT_MODE" in str(attacker_mode):
        # 如果攻击方模式包含"TRANSPORT_MODE"，则在基准随机值上减去一个在[0, 0.1]区间内的随机值
        base_random -= random.uniform(0, 0.1)

    if "FIGHTER_MODE" in str(attacker_mode):
        # 如果攻击方模式包含"FIGHTER_MODE"，则在基准随机值上减去一个在[0, 0.08]区间内的随机值
        base_random -= random.uniform(0, 0.08)

    if "HELICOPTER_MODE" in str(attacker_mode):
        # 如果攻击方模式包含"HELICOPTER_MODE"，则在基准随机值上减去一个在[0, 0.06]区间内的随机值
        base_random -= random.uniform(0, 0.06)

    # 将调整后的 base_random 映射到0或者1
    if base_random > 0.5:
        return 1
    else:
        return 0

def calculate_encounter_time(attacker, now_defender, now_time):
        # 获取初始参数
        v0 = attacker.get_speed(now_time)
        v1 = now_defender.get_speed()
        theta0 = math.radians(attacker.get_direction(now_time))
        h0 = attacker.get_height(now_time)
        d0 = attacker.get_distance(now_time)
        g = 9.8  # 重力加速度
        def f(x,a,b,c,d,e):
            return a*x**4 + b*x**3 + c*x**2+d*x+e
        a = 1/4*g**2
        b = -g*v0
        c = v0*math.cos(theta0)**2+v0**2-g*h0-v1**2
        d = 2*h0*v0-2*d0*v0*math.cos(theta0)
        e = h0**2+d0**2
        def solve_quartic_equation(a, b, c, d, e):
            coefficients = [a, b, c, d, e]
            roots = np.roots(coefficients)
            real_positive_roots = [root.real for root in roots if np.isreal(root) and root > 0]
            return real_positive_roots

        # 示例
        a = 1 / 4 * g ** 2
        b = -g * v0
        c = v0 * np.cos(theta0) ** 2 + v0 ** 2 - g * h0 - v1 ** 2
        d = 2 * h0 * v0 - 2 * d0 * v0 * np.cos(theta0)
        e = h0 ** 2 + d0 ** 2

        # 解一元四次方程并筛选大于零的实数根
        positive_roots = solve_quartic_equation(a, b, c, d, e)
        min_positive_root = float("inf")  # 设置初始值为较大的正无穷大
        if len(positive_roots) == 0:
            print("无法击落")
        else:
            min_positive_root = min(positive_roots)
        return min_positive_root
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
