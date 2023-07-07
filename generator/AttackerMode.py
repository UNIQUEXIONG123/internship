from abc import ABC, abstractmethod

from attacker.plane.Fighter import Fighter


class AbstractAttackerMode(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def generate(self):
        pass


# 三个战斗机
class AttackerMode1(AbstractAttackerMode):
    def generate(self):
        fighter1 = Fighter()
        print('direction', fighter1.get_direction(2))
        print('speed', fighter1.get_speed(2))
        print('heading', fighter1.get_heading(2))
        print('threaten', fighter1.get_threaten_level())

    def __init__(self):
        super().__init__()
        pass


# 三个轰炸机
class AttackerMode2(AbstractAttackerMode):
    def generate(self):
        print("三个轰炸机")

    def __init__(self):
        super().__init__()
        pass


# 三个直升机
class AttackerMode3(AbstractAttackerMode):
    def generate(self):
        print("三个直升机")

    def __init__(self):
        super().__init__()
        pass


# 三个运输机
class AttackerMode4(AbstractAttackerMode):
    def generate(self):
        print("三个运输机")

    def __init__(self):
        super().__init__()
        pass


# 三个超高音速导弹
class AttackerMode5(AbstractAttackerMode):
    def generate(self):
        print("三个超高音速导弹")

    def __init__(self):
        super().__init__()
        pass


# 三个超音速导弹
class AttackerMode6(AbstractAttackerMode):
    def generate(self):
        print("三个超音速导弹")

    def __init__(self):
        super().__init__()
        pass


# 三个亚音速导弹
class AttackerMode7(AbstractAttackerMode):
    def generate(self):
        print("三个亚音速导弹")

    def __init__(self):
        super().__init__()
        pass


class AttackerMode8(AbstractAttackerMode):
    def generate(self):
        print("攻击模式8")

    def __init__(self):
        super().__init__()
        pass


class AttackerMode9(AbstractAttackerMode):
    def generate(self):
        print("攻击模式9")

    def __init__(self):
        super().__init__()
        pass


attacker_mode_dic = {
    1: AttackerMode1,
    2: AttackerMode2,
    3: AttackerMode3,
    4: AttackerMode4,
    5: AttackerMode5,
    6: AttackerMode6,
    7: AttackerMode7,
    8: AttackerMode8,
    9: AttackerMode9
}
