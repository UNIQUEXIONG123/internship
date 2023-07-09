import math
from abc import ABC
from enum import Enum
import random
from utils.Utils import solve_quadratic_equation, ModeNames
from attacker.mode.Mode import ModeAbstract

# 导弹的三种飞行模式，由于三种导弹飞行模式都相同，因此抽出来
# class Mode:
#     STRAIGHT_LINE = 1  # 直线飞行模式
#     PARABOLA = 2  # 抛物线模式
#     DIVE = 3  # 俯冲


class MissileType(Enum):
    SUBSONIC = "Subsonic"
    SUPERSONIC = "Supersonic"
    HYPERSONIC = "Hypersonic"


class MissileModeAbstract(ModeAbstract, ABC):

    def __init__(self):
        super().__init__()


class MissileMode1Abstract(MissileModeAbstract, ABC):
    def __init__(self):
        super().__init__()

    def get_distance(self, t):
        return abs(self.start_distance - self.speed * t)

    def get_height(self, t):
        return self.start_height

    def get_direction(self, t):
        if self.start_distance - self.speed * t >= 0:
            return self.start_direction
        else:
            return (self.start_direction + 180) % 360

    def get_speed(self, t):
        if t == 0:
            return self.start_speed
        return self.speed

    def get_heading(self, t):
        return self.start_heading


# 增加初始抛射角projectile_angle
class MissileMode2Abstract(MissileModeAbstract, ABC):

    def __init__(self):
        super().__init__()
        self.projectile_angle = 0

    def get_distance(self, t):
        distance = abs(self.start_distance - self.speed * math.cos(self.projectile_angle) * t)
        return distance

    def get_height(self, t):
        height = - self.speed * math.sin(self.projectile_angle) * t + 0.5 * 9.8 * t ** 2
        return height

    def get_direction(self, t):
        if abs(self.start_distance - self.speed * math.cos(self.projectile_angle) * t) > 0:
            return self.start_direction
        else:
            return (self.start_direction + 180) % 360

    def get_speed(self, t):
        if t == 0:
            return self.start_speed
        speed_x = math.cos(self.projectile_angle) * self.speed
        speed_y = abs(9.8 * t - math.sin(self.projectile_angle) * t)
        speed = math.sqrt(speed_x ** 2 + speed_y ** 2)
        return speed

    def get_heading(self, t):
        return self.start_heading


class MissileMode3Abstract(MissileModeAbstract, ABC):
    def __init__(self):
        super().__init__()

    def get_distance(self, t):
        # 斜边长
        hypotenuse = math.sqrt(self.start_distance ** 2 + self.start_height ** 2)
        horizontal_velocity = self.start_distance / hypotenuse * self.speed
        return abs(self.start_distance - horizontal_velocity * t)

    def get_height(self, t):
        hypotenuse = math.sqrt(self.start_distance ** 2 + self.start_height ** 2)
        vertical_velocity = self.start_height / hypotenuse * self.speed
        return abs(self.start_height - vertical_velocity * t)

    def get_direction(self, t):
        hypotenuse = math.sqrt(self.start_distance ** 2 + self.start_height ** 2)
        vertical_velocity = self.start_height / hypotenuse * self.speed
        if self.start_height - vertical_velocity * t > 0:
            return self.start_direction
        else:
            return (self.start_direction + 180) % 360

    def get_speed(self, t):
        if t == 0:
            return self.start_speed
        return self.speed

    def get_heading(self, t):
        return self.start_heading


class SubsonicMode1(MissileMode1Abstract):
    def get_threaten_level(self, t):
        return get_missile_threat_level(self.get_distance(t), MissileType.SUBSONIC)

    def __init__(self):
        super().__init__()
        self.start_distance = random.gauss(24000, 2000)  # 18-30公里
        self.start_height = random.gauss(24000, 2000)
        self.start_direction = random.uniform(0, 359)
        self.start_speed = random.gauss(320, 7)  # 300-340
        self.speed = random.gauss(self.start_speed, 1)  # 有一米的误差，这个字段表示在飞行过程中速度保持不变
        self.start_heading = random.gauss(0, 0.33)
        self.start_time = 0
        self.threaten_level = get_missile_threat_level(self.start_distance, MissileType.SUBSONIC)
        self.is_alive = True
        self.mode_name = ModeNames.SUBSONIC_MODE_1

    def generate(self):
        pass


# 所有的斜抛轨迹都增加一个attribute，抛射角：projectile_angle
class SubsonicMode2(MissileMode2Abstract):
    def get_threaten_level(self, t):
        return get_missile_threat_level(self.get_distance(t), MissileType.SUBSONIC)

    def __init__(self):
        super().__init__()
        self.start_distance = random.gauss(24000, 2000)  # 28-40公里
        self.start_height = random.gauss(24000, 2000)
        self.start_direction = random.uniform(0, 359)
        self.start_speed = random.gauss(320, 7)  # 300-340
        self.speed = random.gauss(self.start_speed, 1)  # 有一米的误差，这个字段表示在飞行过程中速度保持不变
        self.start_heading = random.gauss(0, 0.33)
        self.start_time = 0
        self.threaten_level = get_missile_threat_level(self.start_distance, MissileType.SUBSONIC)
        self.is_alive = True
        self.mode_name = ModeNames.SUBSONIC_MODE_2
        a = 0.5 * 9.8 * self.start_distance ** 2 / self.speed ** 2
        b = - self.start_distance
        c = 0.5 * 9.8 * self.start_distance ** 2 / self.speed ** 2 - self.start_height
        root = solve_quadratic_equation(a, b, c)
        if root == -1:
            self.is_alive = False
        else:
            self.projectile_angle = root

    def generate(self):
        pass


class SubsonicMode3(MissileMode3Abstract):
    def get_threaten_level(self, t):
        return get_missile_threat_level(self.get_distance(t), MissileType.SUBSONIC)

    def __init__(self):
        super().__init__()
        self.start_distance = random.gauss(24000, 2000)  # 28-40公里
        self.start_height = random.gauss(24000, 2000)
        self.start_direction = random.uniform(0, 359)
        self.start_speed = random.gauss(320, 7)  # 300-340
        self.speed = random.gauss(self.start_speed, 1)  # 有一米的误差，这个字段表示在飞行过程中速度保持不变
        self.start_heading = random.gauss(0, 0.33)
        self.start_time = 0
        self.threaten_level = get_missile_threat_level(self.start_distance, MissileType.SUBSONIC)
        self.is_alive = True
        self.mode_name = ModeNames.SUBSONIC_MODE_3

    def generate(self):
        pass


class SupersonicMode1(MissileMode1Abstract):
    def get_threaten_level(self, t):
        return get_missile_threat_level(self.get_distance(t), MissileType.SUPERSONIC)

    def __init__(self):
        super().__init__()
        self.start_distance = random.gauss(44000, 2000)  # 44公里左右出现导弹，比飞机远一点
        self.start_height = random.gauss(30000, 1000)  # 低空飞行
        self.start_direction = random.uniform(0, 359)
        self.start_speed = random.gauss(570, 77)  # 340-800
        self.speed = random.gauss(self.start_speed, 1)  # 有一米的误差，这个字段表示在飞行过程中速度保持不变
        self.start_heading = random.gauss(0, 0.33)
        self.start_time = 0
        self.threaten_level = get_missile_threat_level(self.start_distance, MissileType.SUPERSONIC)
        self.is_alive = True
        self.mode_name = ModeNames.SUPERSONIC_MODE_1

    def generate(self):
        pass


class SupersonicMode2(MissileMode2Abstract):
    def get_threaten_level(self, t):
        return get_missile_threat_level(self.get_distance(t), MissileType.SUPERSONIC)

    def __init__(self):
        super().__init__()
        self.start_distance = random.gauss(44000, 2000)  # 44公里左右出现导弹，比飞机远一点
        self.start_height = random.gauss(30000, 1000)  # 低空飞行
        self.start_direction = random.uniform(0, 359)
        self.start_speed = random.gauss(570, 77)  # 340-800
        self.speed = random.gauss(self.start_speed, 1)  # 有一米的误差，这个字段表示在飞行过程中速度保持不变
        self.start_heading = random.gauss(0, 0.33)
        self.start_time = 0
        self.threaten_level = get_missile_threat_level(self.start_distance, MissileType.SUPERSONIC)
        self.is_alive = True
        self.mode_name = ModeNames.SUPERSONIC_MODE_2
        a = 0.5 * 9.8 * self.start_distance ** 2 / self.speed ** 2
        b = - self.start_distance
        c = 0.5 * 9.8 * self.start_distance ** 2 / self.speed ** 2 - self.start_height
        root = solve_quadratic_equation(a, b, c)
        if root == -1:
            self.is_alive = False
        else:
            self.projectile_angle = root

    def generate(self):
        pass


class SupersonicMode3(MissileMode3Abstract):
    def get_threaten_level(self, t):
        return get_missile_threat_level(self.get_distance(t), MissileType.SUPERSONIC)

    def __init__(self):
        super().__init__()
        self.start_distance = random.gauss(44000, 2000)  # 44公里左右出现导弹，比飞机远一点
        self.start_height = random.gauss(30000, 1000)
        self.start_direction = random.uniform(0, 359)
        self.start_speed = random.gauss(570, 77)  # 340-800
        self.speed = random.gauss(self.start_speed, 1)  # 有一米的误差，这个字段表示在飞行过程中速度保持不变
        self.start_heading = random.gauss(0, 0.33)
        self.start_time = 0
        self.threaten_level = get_missile_threat_level(self.start_distance, MissileType.SUPERSONIC)
        self.is_alive = True
        self.mode_name = ModeNames.SUPERSONIC_MODE_3

    def generate(self):
        pass


class HypersonicMode1(MissileMode1Abstract):
    def get_threaten_level(self, t):
        return get_missile_threat_level(self.get_distance(t), MissileType.HYPERSONIC)

    def __init__(self):
        super().__init__()
        self.start_distance = random.gauss(44000, 2000)  # 44公里左右出现导弹，比飞机远一点
        self.start_height = random.gauss(40000, 1000)  # 中空飞行
        self.start_direction = random.uniform(0, 359)
        self.start_speed = random.gauss(1300, 167)  # 800-1600
        self.speed = random.gauss(self.start_speed, 1)  # 有一米的误差，这个字段表示在飞行过程中速度保持不变
        self.start_heading = random.gauss(0, 0.33)
        self.start_time = 0
        self.threaten_level = get_missile_threat_level(self.start_distance, MissileType.HYPERSONIC)
        self.is_alive = True
        self.mode_name = ModeNames.HYPERSONIC_MODE_1

    def generate(self):
        pass


class HypersonicMode2(MissileMode2Abstract):
    def get_threaten_level(self, t):
        return get_missile_threat_level(self.get_distance(t), MissileType.HYPERSONIC)

    def __init__(self):
        super().__init__()
        self.start_distance = random.gauss(44000, 2000)  # 44公里左右出现导弹，比飞机远一点
        self.start_height = random.gauss(40000, 1000)  # 中空飞行
        self.start_direction = random.uniform(0, 359)
        self.start_speed = random.gauss(1300, 167)  # 800-1600
        self.speed = random.gauss(self.start_speed, 1)  # 有一米的误差，这个字段表示在飞行过程中速度保持不变
        self.start_heading = random.gauss(0, 0.33)
        self.start_time = 0
        self.threaten_level = get_missile_threat_level(self.start_distance, MissileType.HYPERSONIC)
        self.is_alive = True
        self.mode_name = ModeNames.HYPERSONIC_MODE_2
        a = 0.5 * 9.8 * self.start_distance ** 2 / self.speed ** 2
        b = - self.start_distance
        c = 0.5 * 9.8 * self.start_distance ** 2 / self.speed ** 2 - self.start_height
        root = solve_quadratic_equation(a, b, c)
        if root == -1:
            self.is_alive = False
        else:
            self.projectile_angle = root

    def generate(self):
        pass


class HypersonicMode3(MissileMode3Abstract):
    def get_threaten_level(self, t):
        return get_missile_threat_level(self.get_distance(t), MissileType.HYPERSONIC)

    def get_distance(self, t):
        # 斜边长
        hypotenuse = math.sqrt(self.start_distance ** 2 + self.start_height ** 2)
        horizontal_velocity = self.start_distance / hypotenuse * self.speed
        return abs(self.start_distance - horizontal_velocity * t)

    def get_height(self, t):
        hypotenuse = math.sqrt(self.start_distance ** 2 + self.start_height ** 2)
        vertical_velocity = self.start_height / hypotenuse * self.speed
        return abs(self.start_height - vertical_velocity * t)

    def get_direction(self, t):
        hypotenuse = math.sqrt(self.start_distance ** 2 + self.start_height ** 2)
        vertical_velocity = self.start_height / hypotenuse * self.speed
        if self.start_height - vertical_velocity * t > 0:
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
        self.start_distance = random.gauss(44000, 2000)  # 44公里左右出现导弹，比飞机远一点
        self.start_height = random.gauss(40000, 1000)  # 中空飞行
        self.start_direction = random.uniform(0, 359)
        self.start_speed = random.gauss(1300, 167)  # 800-1600
        self.speed = random.gauss(self.start_speed, 1)  # 有一米的误差，这个字段表示在飞行过程中速度保持不变
        self.start_heading = random.gauss(0, 0.33)
        self.start_time = 0
        self.threaten_level = get_missile_threat_level(self.start_distance, MissileType.HYPERSONIC)
        self.is_alive = True
        self.mode_name = ModeNames.HYPERSONIC_MODE_3

    def generate(self):
        pass


class DefaultMissileMode(MissileModeAbstract):

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
            "30-100": 1,
            "8-30": 5,
            "6-8": 7,
            "1.5-6": 9,
            "1-1.5": 11,
            "0.1-1": 13
        },
        MissileType.SUPERSONIC: {
            "30-100": 1,
            "8-30": 7,
            "6-8": 9,
            "1.5-6": 11,
            "1-1.5": 13,
            "0.1-1": 15
        },
        MissileType.HYPERSONIC: {
            "30-100": 1,
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
            if start * 1000 <= distance <= end * 1000:
                threaten_level = level
                break

    return threaten_level
