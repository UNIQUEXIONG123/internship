from abc import ABC, abstractmethod
from enum import Enum
import random


# 导弹的三种飞行模式，由于三种导弹飞行模式都相同，因此抽出来
# class Mode:
#     STRAIGHT_LINE = 1  # 直线飞行模式
#     PARABOLA = 2  # 抛物线模式
#     DIVE = 3  # 俯冲


class MissileType(Enum):
    SUBSONIC = "Subsonic"
    SUPERSONIC = "Supersonic"
    HYPERSONIC = "Hypersonic"


class MissileModeAbstract(ABC):

    @abstractmethod
    def set_threaten_level(self, level):
        pass

    def __init__(self):
        pass

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


class SubsonicModeAbstract(MissileModeAbstract, ABC):
    def __init__(self):
        super().__init__()


class SupersonicModeAbstract(MissileModeAbstract, ABC):
    def __init__(self):
        super().__init__()


class HypersonicModeAbstract(MissileModeAbstract, ABC):
    def __init__(self):
        super().__init__()


class SubsonicMode1(SubsonicModeAbstract):
    def set_threaten_level(self, level):
        self.threaten_level = level

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

    def __init__(self):
        super().__init__()
        self.start_distance = random.gauss(44000, 2000)  # 18-40公里
        self.start_height = random.gauss(60, 13)
        self.start_direction = random.uniform(0, 359)
        self.start_speed = random.gauss(320, 7)  # 300-340
        self.speed = random.gauss(self.start_speed, 1)  # 有一米的误差，这个字段表示在飞行过程中速度保持不变
        self.start_heading = random.gauss(0, 0.33)
        self.start_time = 0
        self.threaten_level = get_missile_threat_level(self.start_distance, MissileType.SUBSONIC)
        self.is_alive = True

    def generate(self):
        pass


class SubsonicMode2(SubsonicModeAbstract):
    def set_threaten_level(self, level):
        self.threaten_level = level

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

    def __init__(self):
        super().__init__()
        self.start_distance = random.gauss(44000, 2000)  # 18-40公里
        self.start_height = random.gauss(60, 13)
        self.start_direction = random.uniform(0, 359)
        self.start_speed = random.gauss(320, 7)  # 300-340
        self.speed = random.gauss(self.start_speed, 1)  # 有一米的误差，这个字段表示在飞行过程中速度保持不变
        self.start_heading = random.gauss(0, 0.33)
        self.start_time = 0
        self.threaten_level = get_missile_threat_level(self.start_distance, MissileType.SUBSONIC)
        self.is_alive = True

    def generate(self):
        pass


class SubsonicMode3(SubsonicModeAbstract):
    def set_threaten_level(self, level):
        self.threaten_level = level

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

    def __init__(self):
        super().__init__()
        self.start_distance = random.gauss(44000, 2000)  # 18-40公里
        self.start_height = random.gauss(60, 13)
        self.start_direction = random.uniform(0, 359)
        self.start_speed = random.gauss(320, 7)  # 300-340
        self.speed = random.gauss(self.start_speed, 1)  # 有一米的误差，这个字段表示在飞行过程中速度保持不变
        self.start_heading = random.gauss(0, 0.33)
        self.start_time = 0
        self.threaten_level = get_missile_threat_level(self.start_distance, MissileType.SUBSONIC)
        self.is_alive = True

    def generate(self):
        pass


class SupersonicMode1(SupersonicModeAbstract):
    def set_threaten_level(self, level):
        self.threaten_level = level

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

    def __init__(self):
        super().__init__()
        self.start_distance = random.gauss(44000, 2000)  # 44公里左右出现导弹，比飞机远一点
        self.start_height = random.gauss(550, 150)  # 低空飞行
        self.start_direction = random.uniform(0, 359)
        self.start_speed = random.gauss(570, 77)  # 340-800
        self.speed = random.gauss(self.start_speed, 1)  # 有一米的误差，这个字段表示在飞行过程中速度保持不变
        self.start_heading = random.gauss(0, 0.33)
        self.start_time = 0
        self.threaten_level = get_missile_threat_level(self.start_distance, MissileType.SUPERSONIC)
        self.is_alive = True

    def generate(self):
        pass


class SupersonicMode2(SupersonicModeAbstract):
    def set_threaten_level(self, level):
        self.threaten_level = level

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

    def __init__(self):
        super().__init__()
        self.start_distance = random.gauss(44000, 2000)  # 44公里左右出现导弹，比飞机远一点
        self.start_height = random.gauss(550, 150)  # 低空飞行
        self.start_direction = random.uniform(0, 359)
        self.start_speed = random.gauss(570, 77)  # 340-800
        self.speed = random.gauss(self.start_speed, 1)  # 有一米的误差，这个字段表示在飞行过程中速度保持不变
        self.start_heading = random.gauss(0, 0.33)
        self.start_time = 0
        self.threaten_level = get_missile_threat_level(self.start_distance, MissileType.SUPERSONIC)
        self.is_alive = True

    def generate(self):
        pass


class SupersonicMode3(SupersonicModeAbstract):
    def set_threaten_level(self, level):
        self.threaten_level = level

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

    def __init__(self):
        super().__init__()
        self.start_distance = random.gauss(44000, 2000)  # 44公里左右出现导弹，比飞机远一点
        self.start_height = random.gauss(550, 150)  # 低空飞行
        self.start_direction = random.uniform(0, 359)
        self.start_speed = random.gauss(570, 77)  # 340-800
        self.speed = random.gauss(self.start_speed, 1)  # 有一米的误差，这个字段表示在飞行过程中速度保持不变
        self.start_heading = random.gauss(0, 0.33)
        self.start_time = 0
        self.threaten_level = get_missile_threat_level(self.start_distance, MissileType.SUPERSONIC)
        self.is_alive = True

    def generate(self):
        pass


class HypersonicMode1(HypersonicModeAbstract):
    def set_threaten_level(self, level):
        self.threaten_level = level

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

    def __init__(self):
        super().__init__()
        self.start_distance = random.gauss(44000, 2000)  # 44公里左右出现导弹，比飞机远一点
        self.start_height = random.gauss(4000, 1000)  # 中空飞行
        self.start_direction = random.uniform(0, 359)
        self.start_speed = random.gauss(1300, 167)  # 800-1600
        self.speed = random.gauss(self.start_speed, 1)  # 有一米的误差，这个字段表示在飞行过程中速度保持不变
        self.start_heading = random.gauss(0, 0.33)
        self.start_time = 0
        self.threaten_level = get_missile_threat_level(self.start_distance, MissileType.HYPERSONIC)
        self.is_alive = True

    def generate(self):
        pass


class HypersonicMode2(HypersonicModeAbstract):
    def set_threaten_level(self, level):
        self.threaten_level = level

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

    def __init__(self):
        super().__init__()
        self.start_distance = random.gauss(44000, 2000)  # 44公里左右出现导弹，比飞机远一点
        self.start_height = random.gauss(4000, 1000)  # 中空飞行
        self.start_direction = random.uniform(0, 359)
        self.start_speed = random.gauss(1300, 167)  # 800-1600
        self.speed = random.gauss(self.start_speed, 1)  # 有一米的误差，这个字段表示在飞行过程中速度保持不变
        self.start_heading = random.gauss(0, 0.33)
        self.start_time = 0
        self.threaten_level = get_missile_threat_level(self.start_distance, MissileType.HYPERSONIC)
        self.is_alive = True

    def generate(self):
        pass


class HypersonicMode3(HypersonicModeAbstract):
    def set_threaten_level(self, level):
        self.threaten_level = level

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

    def __init__(self):
        super().__init__()
        self.start_distance = random.gauss(44000, 2000)  # 44公里左右出现导弹，比飞机远一点
        self.start_height = random.gauss(4000, 1000)  # 中空飞行
        self.start_direction = random.uniform(0, 359)
        self.start_speed = random.gauss(1300, 167)  # 800-1600
        self.speed = random.gauss(self.start_speed, 1)  # 有一米的误差，这个字段表示在飞行过程中速度保持不变
        self.start_heading = random.gauss(0, 0.33)
        self.start_time = 0
        self.threaten_level = get_missile_threat_level(self.start_distance, MissileType.HYPERSONIC)
        self.is_alive = True

    def generate(self):
        pass


subsonic_mode_dic = {
    1: SubsonicMode1,
    2: SubsonicMode2,
    3: SubsonicMode3
}

supersonic_mode_dic = {
    1: SupersonicMode1,
    2: SupersonicMode2,
    3: SupersonicMode3
}

hypersonic_mode_dic = {
    1: HypersonicMode1,
    2: HypersonicMode2,
    3: HypersonicMode3
}


def get_missile_threat_level(distance, missile_type):
    missile_dict = {
        MissileType.SUBSONIC: {
            "8-30": 5,
            "6-8": 7,
            "1.5-6": 9,
            "1-1.5": 11,
            "0.1-1": 13
        },
        MissileType.SUPERSONIC: {
            "8-30": 7,
            "6-8": 9,
            "1.5-6": 11,
            "1-1.5": 13,
            "0.1-1": 15
        },
        MissileType.HYPERSONIC: {
            "8-30": 9,
            "6-8": 11,
            "1.5-6": 13,
            "1-1.5": 15,
            "0.1-1": 17
        }
    }

    threaten_level = None

    if missile_type in missile_dict:
        threat_levels = missile_dict[missile_type]

        for range_str, level in threat_levels.items():
            start, end = map(float, range_str.split("-"))
            if start <= distance <= end:
                threaten_level = level
                break

    return threaten_level
