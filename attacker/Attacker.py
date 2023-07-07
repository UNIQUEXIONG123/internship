from abc import ABC, abstractmethod


class Attacker(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_distance(self):
        """
        获取距离
        """
        pass

    @abstractmethod
    def get_height(self):
        """
        获取高度
        """
        pass

    @abstractmethod
    def get_direction(self):
        """
        获取方向
        """
        pass

    @abstractmethod
    def get_speed(self):
        """
        获取速度
        """
        pass

    @abstractmethod
    def get_heading(self):
        """
        获取航向
        """
        pass

    def destroy(self):
        """
        摧毁目标
        """
        pass

    def set_threaten_level(self, level):
        """
        设置威胁级别
        """
        pass
