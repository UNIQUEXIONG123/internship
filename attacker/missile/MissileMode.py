from abc import ABC, abstractmethod


# 导弹的三种飞行模式，由于三种导弹飞行模式都相同，因此抽出来
# class Mode:
#     STRAIGHT_LINE = 1  # 直线飞行模式
#     PARABOLA = 2  # 抛物线模式
#     DIVE = 3  # 俯冲


class MissileModeAbstract(ABC):

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
        pass

    def generate(self):
        pass


class SubsonicMode2(SubsonicModeAbstract):
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
        pass

    def generate(self):
        pass


class SubsonicMode3(SubsonicModeAbstract):
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
        pass

    def generate(self):
        pass


class SupersonicMode1(SupersonicModeAbstract):
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
        pass

    def generate(self):
        pass


class SupersonicMode2(SupersonicModeAbstract):
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
        pass

    def generate(self):
        pass


class SupersonicMode3(SupersonicModeAbstract):
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
        pass

    def generate(self):
        pass


class HypersonicMode1(HypersonicModeAbstract):
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
        pass

    def generate(self):
        pass


class HypersonicMode2(HypersonicModeAbstract):
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
        pass

    def generate(self):
        pass


class HypersonicMode3(HypersonicModeAbstract):
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
        pass

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
