from abc import ABC, abstractmethod

from attacker.plane.Fighter import Fighter
from attacker.plane.Bomber import Bomber
from attacker.plane.Helicopter import Helicopter
from attacker.plane.Transport import Transport
from attacker.missile.Subsonic import Subsonic
from attacker.missile.Supersonic import Supersonic
from attacker.missile.Hypersonic import Hypersonic


class AbstractAttackerMode(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def generate(self):
        pass


# 2个战斗机
class AttackerMode1(AbstractAttackerMode):
    def generate(self):
        fighter1 = Fighter()
        fighter2 = Fighter()
        return fighter1, fighter2

    def __init__(self):
        super().__init__()
        pass


# 2个轰炸机
class AttackerMode2(AbstractAttackerMode):
    def generate(self):
        bomber1 = Bomber()
        bomber2 = Bomber()
        return bomber1, bomber2

    def __init__(self):
        super().__init__()
        pass


# 2个直升机
class AttackerMode3(AbstractAttackerMode):
    def generate(self):
        helicopter1 = Helicopter()
        helicopter2 = Helicopter()
        return helicopter1, helicopter2

    def __init__(self):
        super().__init__()
        pass


# 2个运输机
class AttackerMode4(AbstractAttackerMode):
    def generate(self):
        transport1 = Transport()
        transport2 = Transport()
        return transport1, transport2

    def __init__(self):
        super().__init__()
        pass


# 2个亚音速导弹
class AttackerMode5(AbstractAttackerMode):
    def generate(self):
        subsonic1 = Subsonic(1)
        subsonic2 = Subsonic(2)
        return subsonic1, subsonic2

    def __init__(self):
        super().__init__()
        pass


# 2个超音速导弹
class AttackerMode6(AbstractAttackerMode):
    def generate(self):
        supersonic1 = Supersonic(1)
        supersonic2 = Supersonic(2)
        return supersonic1, supersonic2

    def __init__(self):
        super().__init__()
        pass


# 2个高超音速导弹
class AttackerMode7(AbstractAttackerMode):
    def generate(self):
        hypersonic1 = Hypersonic(1)
        hypersonic2 = Hypersonic(2)
        return hypersonic1, hypersonic2

    def __init__(self):
        super().__init__()
        pass


# 一个直升机
class AttackerMode8(AbstractAttackerMode):
    def generate(self):
        helicopter = Helicopter()
        return helicopter

    def __init__(self):
        super().__init__()
        pass


# 一个轰炸机
class AttackerMode9(AbstractAttackerMode):
    def generate(self):
        bomber = Bomber()
        return bomber

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
