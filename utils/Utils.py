import math
from enum import Enum


def solve_quadratic_equation(a, b, c):
    """
    解二次方程工具函数
    :param a: 二次方程二次项系数
    :param b: 二次方程一次项系数
    :param c: 二次方程零次项系数
    :return: -1： 无解， >0有唯一解，不考虑斜下抛
    """
    # 计算判别式
    discriminant = b ** 2 - 4 * a * c

    # 判别式小于0，方程无实数根
    if discriminant < 0:
        return -1

    # 判别式等于0，方程有一个实数根
    elif discriminant == 0:
        root = -b / (2 * a)
        return root

    # 判别式大于0，方程有两个实数根
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        if root1 > 0:
            return root1
        elif root2 > 0:
            return root2
        return -1


# 用于返回进攻方的攻击种类
class AttackerTypes(Enum):
    DEFAULT_TYPE = "DEFAULT_TYPE"
    SUBSONIC = "Subsonic"
    SUPERSONIC = "Supersonic"
    HYPERSONIC = "Hypersonic"
    TRANSPORT = "Transport"
    HELICOPTER = "Helicopter"
    FIGHTER = "Fighter"
    BOMBER = "Bomber"


# 用于返回攻击模式
class ModeNames(Enum):
    DEFAULT_MODE_NAME = "DEFAULT_MODE_NAME"

    SUBSONIC_MODE_1 = "SubsonicMode1"
    SUBSONIC_MODE_2 = "SubsonicMode2"
    SUBSONIC_MODE_3 = "SubsonicMode3"

    SUPERSONIC_MODE_1 = "SupersonicMode1"
    SUPERSONIC_MODE_2 = "SupersonicMode2"
    SUPERSONIC_MODE_3 = "SupersonicMode3"

    HYPERSONIC_MODE_1 = "HypersonicMode1"
    HYPERSONIC_MODE_2 = "HypersonicMode2"
    HYPERSONIC_MODE_3 = "HypersonicMode3"

    BOMBER_MODE = "BomberMode"
    FIGHTER_MODE = "FighterMode"
    HELICOPTER_MODE = "HelicopterMode"
    TRANSPORT_MODE = "TransportMode"

class DefenderTypes(Enum):
    DEFAULT_TYPE = "DEFAULT_TYPE"
    MRAD = "MRAD"
    SCNG = "SCNG"
    SRAD = "SRAD"
    MC = "MC"