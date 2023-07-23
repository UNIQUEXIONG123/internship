import math
import random
from abc import ABC
from enum import Enum

from attacker.mode.Mode import ModeAbstract
from utils.Utils import ModeNames


class AircraftType(Enum):
    TRANSPORT = "Transport"
    HELICOPTER = "Helicopter"
    FIGHTER = "Fighter"
    BOMBER = "Bomber"


class PlaneModeAbstract(ModeAbstract, ABC):

    def __init__(self):
        super().__init__()
        self.counter_measure = 0

    def get_countermeasure(self):
        return self.counter_measure


class BomberModeAbstract(PlaneModeAbstract, ABC):

    def __init__(self):
        super().__init__()
        self.mode_name = ModeNames.BOMBER_MODE


class FighterModeAbstract(PlaneModeAbstract, ABC):
    def __init__(self):
        super().__init__()
        self.mode_name = ModeNames.FIGHTER_MODE


class HelicopterAbstract(PlaneModeAbstract, ABC):
    def __init__(self):
        super().__init__()
        self.mode_name = ModeNames.HELICOPTER_MODE


class TransportAbstract(PlaneModeAbstract, ABC):
    def __init__(self):
        super().__init__()
        self.mode_name = ModeNames.TRANSPORT_MODE
        pass


class BomberMode(BomberModeAbstract):
    def get_threaten_level(self, t):
        """获取轰炸机在时间t的威胁级别。

        参数:
        t (float): 时间，单位为秒。

        返回:
        int: 表示威胁级别的整数值。
        """
        return get_plane_threat_level(self.get_distance(t), AircraftType.BOMBER)

    def __init__(self):
        """BomberMode的构造函数。

        该构造函数用于初始化BomberMode对象的属性。
        """
        super().__init__()
        self.start_distance = random.gauss(29000, 3670)  # 随机生成18-40公里的起始距离
        self.start_height = random.gauss(9000, 1000)  # 随机生成起始高度，均值为9000米，标准差为1000米
        self.start_direction = random.uniform(0, 359)  # 随机生成起始方向，范围为0-359度
        self.start_speed = random.gauss(335, 38)  # 随机生成起始速度，均值为335米/秒，标准差为38米/秒
        self.speed = random.gauss(self.start_speed, 1)  # 随机生成速度，有一米的误差，该字段表示在飞行过程中速度保持不变
        self.start_heading = random.gauss(0, 0.33)  # 随机生成起始航向，均值为0度，标准差为0.33度
        self.start_time = 0  # 初始时间为0秒
        self.threaten_level = get_plane_threat_level(self.start_distance, AircraftType.BOMBER)  # 计算起始距离对应的威胁级别
        self.is_alive = True  # 初始时，飞机存活状态为True
        self.countermeasure = 2  # 威胁级别为2时的对抗措施数量

    def get_distance(self, t):
        """计算飞机在时间t的飞行距离。

        参数:
        t (float): 时间，单位为秒。

        返回:
        float: 飞机在时间t的飞行距离，单位为米。
        """
        return abs(self.start_distance - self.speed * t)

    def get_height(self, t):
        """获取飞机在时间t的高度。

        参数:
        t (float): 时间，单位为秒。

        返回:
        float: 飞机在时间t的高度，单位为米。
        """
        return self.start_height

    def get_direction(self, t):
        """获取飞机在时间t的方向。

        参数:
        t (float): 时间，单位为秒。

        返回:
        float: 飞机在时间t的方向，单位为度。
        """
        if self.start_distance - self.speed * t > 0:
            return self.start_direction
        else:
            return (self.start_direction + 180) % 360

    def get_speed(self, t):
        """获取飞机在时间t的速度。

        参数:
        t (float): 时间，单位为秒。

        返回:
        float: 飞机在时间t的速度，单位为米/秒。
        """
        if t == 0:
            return self.start_speed
        return self.speed

    def get_heading(self, t):
        """获取飞机在时间t的航向。

        参数:
        t (float): 时间，单位为秒。

        返回:
        float: 飞机在时间t的航向，单位为度。
        """
        return self.start_heading

    def generate(self):
        """生成飞机模式的具体行为。

        该方法在这里没有具体的实现，因为BomberMode的行为在其他地方处理。
        """
        pass


# 轰炸机的直线飞行模式

# 攻击机俯冲飞行模式
class FighterMode(FighterModeAbstract):
    def get_threaten_level(self, t):
        return get_plane_threat_level(self.get_distance(t), AircraftType.FIGHTER)

    # 方法用于获取战斗机在时间 't' 时的当前距离。
    # 通过勾股定理计算斜边长，然后使用水平速度和时间 't' 计算水平方向上飞行的距离。
    # 距离的计算是战斗机初始距离（self.start_distance）与水平飞行距离之间的绝对差值。
    def get_distance(self, t):
        hypotenuse = math.sqrt(self.start_distance ** 2 + self.start_height ** 2)
        horizontal_velocity = self.start_distance / hypotenuse * self.speed
        return abs(self.start_distance - horizontal_velocity * t)

    # 方法用于获取战斗机在时间 't' 时的当前高度。
    # 通过勾股定理计算斜边长，然后使用垂直速度和时间 't' 计算垂直方向上飞行的高度。
    # 高度的计算是战斗机初始高度（self.start_height）与垂直飞行高度之间的绝对差值。
    def get_height(self, t):
        hypotenuse = math.sqrt(self.start_distance ** 2 + self.start_height ** 2)
        vertical_velocity = self.start_height / hypotenuse * self.speed
        return abs(self.start_height - vertical_velocity * t)

    # 方法用于获取战斗机在时间 't' 时的当前飞行方向。
    # 通过勾股定理计算斜边长，然后使用垂直速度和时间 't' 计算垂直方向上飞行的高度。
    # 如果战斗机尚未到达目标，则保持初始飞行方向（self.start_direction）。
    # 如果战斗机已经到达目标，则通过添加180度来反转飞行方向。
    def get_direction(self, t):
        hypotenuse = math.sqrt(self.start_distance ** 2 + self.start_height ** 2)
        vertical_velocity = self.start_height / hypotenuse * self.speed
        if self.start_height - vertical_velocity * t > 0:
            return self.start_direction
        else:
            return (self.start_direction + 180) % 360

    # 方法用于获取战斗机在时间 't' 时的当前速度。
    # 我们假设战斗机的速度保持不变，因此返回初始速度（self.start_speed）。
    # 如果 t 为 0，则返回初始速度；否则，返回常数速度（self.speed）。
    def get_speed(self, t):
        if t == 0:
            return self.start_speed
        return self.speed

    # 方法用于获取战斗机在时间 't' 时的当前朝向（方向角）。
    # 我们假设战斗机的朝向保持不变，因此返回初始朝向（self.start_heading）。
    def get_heading(self, t):
        return self.start_heading


    def __init__(self):
        super().__init__()
        self.start_distance = random.gauss(29000, 3670)
        self.start_height = random.gauss(5500, 500)
        self.start_direction = random.uniform(0, 359)
        self.start_speed = random.gauss(600, 67)
        self.speed = random.gauss(self.start_speed, 1)  # 有一米的误差，这个字段表示在飞行过程中速度保持不变
        self.start_heading = random.gauss(0, 0.33)
        self.start_time = 0
        self.threaten_level = get_plane_threat_level(self.start_distance, AircraftType.FIGHTER)
        self.is_alive = True
        self.countermeasure = 4

    def generate(self):
        pass


# 直升机的俯冲飞行模式
class HelicopterMode(HelicopterAbstract):
    def get_threaten_level(self, t):
        return get_plane_threat_level(self.get_distance(t), AircraftType.HELICOPTER)

    def get_distance(self, t):
        return abs(self.start_distance - self.speed * t)

    def get_height(self, t):
        return self.start_height

    def get_direction(self, t):
        if self.start_distance - self.speed * t > 0:
            return self.start_direction
        else:
            return (self.start_direction + 180) % 360

    def get_speed(self, t):
        if t == 0:
            return self.start_speed
        return self.speed

    def get_heading(self, t):
        return self.start_heading

    # 直升机的高度设置de很低，掠海高度
    def __init__(self):
        super().__init__()
        self.start_distance = random.gauss(20000, 3333)  # 路径和轰炸机一样，但是更低
        self.start_height = random.gauss(500, 20)
        self.start_direction = random.uniform(0, 359)
        self.start_speed = random.gauss(95, 8)
        self.speed = random.gauss(self.start_speed, 1)  # 有一米的误差，这个字段表示在飞行过程中速度保持不变
        self.start_heading = random.gauss(0, 0.33)
        self.start_time = 0
        self.threaten_level = get_plane_threat_level(self.start_distance, AircraftType.HELICOPTER)
        self.is_alive = True
        self.countermeasure = 1

    def generate(self):
        pass


# 运输机的高空直线飞行模式
class TransportMode(TransportAbstract):
    def get_threaten_level(self, t):
        return get_plane_threat_level(self.get_distance(t), AircraftType.TRANSPORT)

    def get_distance(self, t):
        return abs(self.start_distance - self.speed * t)

    def get_height(self, t):
        return self.start_height

    def get_direction(self, t):
        if self.start_distance - self.speed * t > 0:
            return self.start_direction
        else:
            return (self.start_direction + 180) % 360

    def get_speed(self, t):
        if t == 0:
            return self.start_speed
        return self.speed

    def get_heading(self, t):
        return self.start_heading

    def __init__(self):
        super().__init__()
        self.start_distance = random.gauss(29000, 3670)
        self.start_height = random.gauss(12500, 1833)
        self.start_direction = random.uniform(0, 359)
        self.start_speed = random.gauss(225, 8)
        self.speed = random.gauss(self.start_speed, 1)  # 有一米的误差，这个字段表示在飞行过程中速度保持不变
        self.start_heading = random.gauss(0, 0.33)
        self.start_time = 0
        self.threaten_level = get_plane_threat_level(self.start_distance, AircraftType.TRANSPORT)
        self.is_alive = True
        self.countermeasure = 0

    def generate(self):
        pass


class DefaultPlaneMode(PlaneModeAbstract):

    def generate(self):
        pass

    def get_distance(self, t):
        return 0

    def get_height(self, t):
        return 0

    def get_direction(self, t):
        return 0

    def get_speed(self, t):
        return 0

    def get_heading(self, t):
        return 0

    def get_threaten_level(self, t):
        return 0


plane_mode_dic = {
    1: BomberMode,
    2: FighterMode,
    3: HelicopterMode,
    4: TransportMode
}


def get_plane_threat_level(distance, aircraft_type):
    threat_levels = {
        AircraftType.TRANSPORT: {
            "30-100": 1,
            "8-30": 2,
            "6-8": 3,
            "1.5-6": 4,
            "1-1.5": 5,
            "0.1-1": 6
        },
        AircraftType.HELICOPTER: {
            "30-100": 1,
            "8-30": 2,
            "6-8": 3,
            "1.5-6": 4,
            "1-1.5": 5,
            "0.1-1": 6
        },
        AircraftType.FIGHTER: {
            "30-100": 1,
            "8-30": 3,
            "6-8": 4,
            "1.5-6": 5,
            "1-1.5": 6,
            "0.1-1": 7
        },
        AircraftType.BOMBER: {
            "30-100": 1,
            "8-30": 2,
            "6-8": 3,
            "1.5-6": 5,
            "1-1.5": 7,
            "0.1-1": 9
        }
    }

    threaten_level = None

    for range_str, level in threat_levels[aircraft_type].items():
        start, end = map(float, range_str.split("-"))
        if start * 1000 <= distance <= end * 1000:
            threaten_level = level
            break

    return threaten_level
