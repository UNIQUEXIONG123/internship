from abc import ABC, abstractmethod


class PlaneModeAbstract(ABC):
    def __init__(self, start_distance, start_height, start_direction, start_speed, start_heading, start_time,
                 max_height, min_height, max_speed, min_speed, threaten_level, is_alive):
        self.start_distance = start_distance
        self.start_height = start_height
        self.start_direction = start_direction
        self.start_speed = start_speed
        self.start_heading = start_heading
        self.start_time = start_time
        self.max_height = max_height
        self.min_height = min_height
        self.max_speed = max_speed
        self.min_speed = min_speed
        self.threaten_level = threaten_level
        self.is_alive = is_alive
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
        pass

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
        pass

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

    def generate(self):
        pass

plane_mode_dic = {
    1: BomberMode,
    2: FighterMode,
    3: HelicopterMode,
    4: TransportMode
}
