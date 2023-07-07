import random
from abc import ABC, abstractmethod


class PlaneModeAbstract(ABC):
    def __init__(self):
        pass

    # 生成实体实际数据
    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def get_distance(self):
        pass

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def get_direction(self):
        pass

    @abstractmethod
    def get_speed(self):
        pass

    @abstractmethod
    def get_heading(self):
        pass

    @abstractmethod
    def get_countermeasure(self):
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
    def __init__(self):
        super().__init__()
        self.start_distance = 1
        self.start_height = 1
        self.start_direction = 1
        self.start_speed = 1
        self.start_heading = 1
        self.start_time = 1
        self.max_height = 1
        self.min_height = 1
        self.max_speed = 1
        self.min_speed = 1
        self.threaten_level = 1
        self.is_alive = True
        self.countermeasure = 1

    def get_distance(self):
        pass

    def get_height(self):
        pass

    def get_direction(self):
        pass

    def get_speed(self):
        pass

    def get_heading(self):
        pass

    def get_countermeasure(self):
        pass

    def generate(self):
        pass


# 攻击机俯冲飞行模式
class FighterMode(FighterModeAbstract):
    def get_distance(self):
        pass

    def get_height(self):
        pass

    def get_direction(self):
        pass

    def get_speed(self):
        pass

    def get_heading(self):
        pass

    def get_countermeasure(self):
        pass

    def __init__(self):
        super().__init__()
        self.start_distance = 1
        self.start_height = 1
        self.start_direction = 1
        self.start_speed = 1
        self.start_heading = 1
        self.start_time = 1
        self.max_height = 1
        self.min_height = 1
        self.max_speed = 1
        self.min_speed = 1
        self.threaten_level = 1
        self.is_alive = True
        self.countermeasure = 1

    def generate(self):
        pass


# 直升机的俯冲飞行模式
class HelicopterMode(HelicopterAbstract):
    def get_height(self):
        pass

    def get_direction(self):
        pass

    def get_speed(self):
        pass

    def get_heading(self):
        pass

    def get_countermeasure(self):
        pass

    def get_distance(self):
        pass

    def __init__(self):
        super().__init__()
        self.start_distance = 1
        self.start_height = 1
        self.start_direction = 1
        self.start_speed = 1
        self.start_heading = 1
        self.start_time = 1
        self.max_height = 1
        self.min_height = 1
        self.max_speed = 1
        self.min_speed = 1
        self.threaten_level = 1
        self.is_alive = True
        self.countermeasure = 1

    def generate(self):
        pass


# 运输机的高空直线飞行模式
class TransportMode(TransportAbstract):
    def get_distance(self):
        pass

    def get_height(self):
        pass

    def get_direction(self):
        pass

    def get_speed(self):
        pass

    def get_heading(self):
        pass

    def get_countermeasure(self):
        pass

    def __init__(self):
        super().__init__()
        self.start_distance = 1
        self.start_height = 1
        self.start_direction = 1
        self.start_speed = random.gauss(225, 8)
        self.start_heading = 1
        self.start_time = 1
        self.max_height = 1
        self.min_height = 1
        self.max_speed = 1
        self.min_speed = 1
        self.threaten_level = 1
        self.is_alive = True
        self.countermeasure = 1

    def generate(self):
        pass


plane_mode_dic = {
    1: BomberMode,
    2: FighterMode,
    3: HelicopterMode,
    4: TransportMode
}
