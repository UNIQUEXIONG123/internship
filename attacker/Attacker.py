from abc import ABC, abstractmethod


class Attacker(ABC):
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
        self.threaten_level = level
