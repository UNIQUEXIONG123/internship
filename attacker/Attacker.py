from abc import ABC, abstractmethod


class Attacker(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_distance(self, t):
        """
        获取距离
        """
        pass

    @abstractmethod
    def get_height(self, t):
        """
        获取高度
        """
        pass

    @abstractmethod
    def get_direction(self, t):
        """
        获取方向
        """
        pass

    @abstractmethod
    def get_speed(self, t):
        """
        获取速度
        """
        pass

    @abstractmethod
    def get_heading(self, t):
        """
        获取航向
        """
        pass

    def destroy(self):
        """
        摧毁目标
        """
        pass

    @abstractmethod
    def set_threaten_level(self, level):
        """
        设置威胁级别
        """
        pass

    @abstractmethod
    def get_threaten_level(self):
        pass
