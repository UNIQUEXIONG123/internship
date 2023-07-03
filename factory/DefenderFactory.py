import random

from defender.MRAD import MRAD
from defender.SCNG import SCNG
from defender.SRAD import SRAD


class DefenderFactory:
    def __init__(self, mrad_animation, srad_animation, scng_animation):
        # 分配队列
        self.allocate_list = []
        # 发射队列
        self.launch_list = []
        # 记录弹药量
        self.animation_map = {
            "mrad_animation": mrad_animation,
            "srad_animation": srad_animation,
            "scng_animation": scng_animation
        }


    def generate(self):
        """
        生成防御器材
        """
        # 生成MRAD
        for _ in range(self.animation_map["mrad_animation"]):
            speed = random.gauss(1000, 500)  # 使用高斯分布生成速度
            delay = random.gauss(0.5, 0.1)  # 使用高斯分布生成延迟
            mrad = MRAD(speed, delay)  # 创建MRAD对象
            self.allocate_list.append(mrad)  # 将MRAD对象添加到分配队列中

        # 生成SRAD
        for _ in range(self.animation_map["srad_animation"]):
            speed = random.gauss(800, 200)  # 使用高斯分布生成速度
            delay = random.gauss(0.8, 0.2)  # 使用高斯分布生成延迟
            srad = SRAD(speed, delay)  # 创建SRAD对象
            self.allocate_list.append(srad)  # 将SRAD对象添加到分配队列中

        # 生成SCNG
        for _ in range(self.animation_map["scng_animation"]):
            speed = random.gauss(500, 100)  # 使用高斯分布生成速度
            angular_velocity = random.gauss(0.5, 0.1)  # 使用高斯分布生成角速度
            scng = SCNG(speed, angular_velocity)  # 创建SCNG对象
            self.allocate_list.append(scng)  # 将SCNG对象添加到分配队列中

    def allocate_defenders(self):
        """
        将防御器材从分配队列移到发射队列
        """
        self.launch_list.extend(self.allocate_list)  # 将分配队列中的防御器材添加到发射队列中
        self.allocate_list = []  # 清空分配队列

    def print_defenders(self):
        """
        打印发射队列中的防御器材信息
        """
        for defender in self.launch_list:
            print(defender)

# 使用示例
mrad_animation = 10
srad_animation = 5
scng_animation = 3

factory = DefenderFactory(mrad_animation, srad_animation, scng_animation)
factory.generate()
factory.allocate_defenders()
factory.print_defenders()
