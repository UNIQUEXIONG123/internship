from abc import abstractmethod, ABC

from utils.Utils import ModeNames


class ModeAbstract(ABC):
    def __init__(self):
        self.start_distance = 0
        self.start_height = 0
        self.start_direction = 0
        self.start_speed = 0
        self.speed = 0
        self.start_heading = 0
        self.start_time = 0
        self.threaten_level = 0
        self.is_alive = True
        self.mode_name = ModeNames.DEFAULT_MODE_NAME  # 认为是一个默认的，没什么用

    def set_threaten_level(self, level):
        self.threaten_level = level

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

    @abstractmethod
    def get_threaten_level(self, t):
        pass

    def get_mode_name(self):
        return self.mode_name


class DefaultMode(ModeAbstract):
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
