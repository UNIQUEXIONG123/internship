import random
from abc import ABC, abstractmethod
from enum import Enum


class AircraftType(Enum):
    TRANSPORT = "Transport"
    HELICOPTER = "Helicopter"
    FIGHTER = "Fighter"
    BOMBER = "Bomber"


class PlaneModeAbstract(ABC):
    def __init__(self):
        pass

    # 生成实体实际数据
    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def get_distance(self, t):
        pass

    @abstractmethod
    def get_height(self, t):
        pass

    @abstractmethod
    def get_direction(self, t):
        pass

    @abstractmethod
    def get_speed(self, t):
        pass

    @abstractmethod
    def get_heading(self, t):
        pass

    @abstractmethod
    def get_countermeasure(self, t):
        pass

    @abstractmethod
    def set_threaten_level(self, level):
        pass


class BomberModeAbstract(PlaneModeAbstract, ABC):
    def __init__(self):
        """
        生成
        """
        super().__init__()
        pass


class FighterModeAbstract(PlaneModeAbstract, ABC):
    def __init__(self):
        super().__init__()
        pass


class HelicopterAbstract(PlaneModeAbstract, ABC):
    def __init__(self):
        super().__init__()
        pass


class TransportAbstract(PlaneModeAbstract, ABC):
    def __init__(self):
        super().__init__()
        pass


# 轰炸机的直线飞行模式
class BomberMode(BomberModeAbstract):
    def set_threaten_level(self, level):
        self.threaten_level = level

    def __init__(self):
        super().__init__()
        self.start_distance = random.gauss(29000, 3670)  # 18-40公里
        self.start_height = random.gauss(550, 90)
        self.start_direction = random.uniform(0, 359)
        self.start_speed = random.gauss(335, 38)
        self.speed = random.gauss(self.start_speed, 1)  # 有一米的误差，这个字段表示在飞行过程中速度保持不变
        self.start_heading = random.gauss(0, 0.33)
        self.start_time = 0
        self.threaten_level = get_plane_threat_level(self.start_distance, AircraftType.BOMBER)
        self.is_alive = True
        self.countermeasure = 2

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
        return self.speed

    def get_heading(self, t):
        return self.start_heading

    def get_countermeasure(self, t):
        return self.countermeasure

    def generate(self):
        pass


# 攻击机俯冲飞行模式
class FighterMode(FighterModeAbstract):
    def set_threaten_level(self, level):
        pass

    def get_distance(self, t):
        pass

    def get_height(self, t):
        pass

    def get_direction(self, t):
        pass

    def get_speed(self, t):
        pass

    def get_heading(self, t):
        pass

    def get_countermeasure(self, t):
        pass

    def __init__(self):
        super().__init__()
        self.start_distance = random.gauss(29000, 3670)
        self.start_height = random.gauss(1050, 317)
        self.start_direction = random.uniform(0, 359)
        self.start_speed = random.gauss(600, 67)
        self.start_heading = random.gauss(0, 0.33)
        self.start_time = 0
        self.threaten_level = get_plane_threat_level(self.start_distance, AircraftType.FIGHTER)
        self.is_alive = True
        self.countermeasure = 4

    def generate(self):
        pass


# 直升机的俯冲飞行模式
class HelicopterMode(HelicopterAbstract):
    def set_threaten_level(self, level):
        self.threaten_level = level

    def get_height(self, t):
        pass

    def get_direction(self, t):
        pass

    def get_speed(self, t):
        pass

    def get_heading(self, t):
        pass

    def get_countermeasure(self, t):
        pass

    def get_distance(self, t):
        pass

    def __init__(self):
        super().__init__()
        self.start_distance = random.gauss(29000, 3670)
        self.start_height = random.gauss(225, 58)
        self.start_direction = random.uniform(0, 359)
        self.start_speed = random.gauss(95, 8)
        self.start_heading = random.gauss(0, 0.33)
        self.start_time = 0
        self.threaten_level = get_plane_threat_level(self.start_distance, AircraftType.HELICOPTER)
        self.is_alive = True
        self.countermeasure = 1

    def generate(self):
        pass


# 运输机的高空直线飞行模式
class TransportMode(TransportAbstract):
    def set_threaten_level(self, level):
        pass

    def get_distance(self, t):
        pass

    def get_height(self, t):
        pass

    def get_direction(self, t):
        pass

    def get_speed(self, t):
        pass

    def get_heading(self, t):
        pass

    def get_countermeasure(self, t):
        return 0

    def __init__(self):
        super().__init__()
        self.start_distance = random.gauss(29000, 3670)
        self.start_height = random.gauss(12500, 833)
        self.start_direction = random.uniform(0, 359)
        self.start_speed = random.gauss(225, 8)
        self.start_heading = random.gauss(0, 0.33)
        self.start_time = 0
        self.threaten_level = get_plane_threat_level(self.start_distance, AircraftType.TRANSPORT)
        self.is_alive = True
        self.countermeasure = 0

    def generate(self):
        pass


plane_mode_dic = {
    1: BomberMode,
    2: FighterMode,
    3: HelicopterMode,
    4: TransportMode
}


def get_plane_threat_level(distance, aircraft_type):
    threat_levels = {
        AircraftType.TRANSPORT: {
            "8-30": 2,
            "6-8": 3,
            "1.5-6": 4,
            "1-1.5": 5,
            "0.1-1": 6
        },
        AircraftType.HELICOPTER: {
            "8-30": 2,
            "6-8": 3,
            "1.5-6": 4,
            "1-1.5": 5,
            "0.1-1": 6
        },
        AircraftType.FIGHTER: {
            "8-30": 3,
            "6-8": 4,
            "1.5-6": 5,
            "1-1.5": 6,
            "0.1-1": 7
        },
        AircraftType.BOMBER: {
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
        if start <= distance <= end:
            threaten_level = level
            break

    return threaten_level
