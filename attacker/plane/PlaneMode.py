from abc import ABC, abstractmethod


class PlaneModeAbstract(ABC):
    def __init__(self):
        pass

    # 生成实体实际数据
    @abstractmethod
    def generate(self):
        pass


class BomberModeAbstract(ABC, PlaneModeAbstract):
    def __init__(self):
        pass


class FighterModeAbstract(ABC, PlaneModeAbstract):
    def __init__(self):
        pass


class HelicopterAbstract(ABC, PlaneModeAbstract):
    def __init__(self):
        pass


class TransportAbstract(ABC, PlaneModeAbstract):
    def __init__(self):
        pass


# 直线飞行模式
class BomberMode1(BomberModeAbstract):
    def __init__(self):
        super().__init__()
        pass

    def generate(self):
        pass


# 俯冲模式
class BomberMode2(BomberModeAbstract):
    def __init__(self):
        super().__init__()
        pass

    def generate(self):
        pass


# 低空飞行模式
class BomberMode3(BomberModeAbstract):
    def __init__(self):
        super().__init__()
        pass

    def generate(self):
        pass


# 直线飞行模式
class FighterMode1(FighterModeAbstract):
    def __init__(self):
        super().__init__()
        pass

    def generate(self):
        pass


# 俯冲模式，到最低的点的时候使用栈道的方式进行逃逸
class FighterMode2(FighterModeAbstract):
    def __init__(self):
        super().__init__()
        pass

    def generate(self):
        pass


# 低空飞行模式，逃逸时采用栈道逃逸
class FighterMode3(FighterModeAbstract):
    def __init__(self):
        super().__init__()
        pass

    def generate(self):
        pass


# 直线模式
class HelicopterMode1(HelicopterAbstract):
    def __init__(self):
        super().__init__()
        pass

    def generate(self):
        pass


# 低空模式
class HelicopterMode2(HelicopterAbstract):
    def __init__(self):
        super().__init__()
        pass

    def generate(self):
        pass


# 栈道模式
class HelicopterMode3(HelicopterAbstract):
    def __init__(self):
        super().__init__()
        pass

    def generate(self):
        pass


# 高空直线飞行
class TransportMode(TransportAbstract):
    def __init__(self):
        super().__init__()

    def generate(self):
        pass


bomber_mode_dic = {
    1: BomberMode1,
    2: BomberMode2,
    3: BomberMode3
}

fighter_mode_dic = {
    1: FighterMode1,
    2: FighterMode2,
    3: FighterMode3
}

helicopter_mode_dic = {
    1: HelicopterMode1,
    2: HelicopterMode2,
    3: HelicopterMode3
}

transport_mode_dic = {
    1: TransportMode
}
