from abc import ABC, abstractmethod


class AbstractAttackerMode(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def generate(self):
        pass


# 三个战斗机
class AttackerMode1(AbstractAttackerMode):
    def generate(self):
        for i in range(3):
            pass
            # fighter1 = Fighter()
            # fighter2 = Fighter()
            # fighter3 = Fighter()

        print("三个战斗机")

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


AttackerModeDic = {
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
