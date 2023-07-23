from abc import ABC
from attacker.mode.Mode import DefaultMode
from utils.Utils import AttackerTypes
class Attacker(ABC):
    def __init__(self):
        self.type = AttackerTypes.DEFAULT_TYPE
        self.mode = DefaultMode()
    def get_distance(self, t):
        """
        获取距离
        """
        return self.mode.get_distance(t)
    def get_height(self, t):
        """
        获取高度
        """
        return self.mode.get_height(t)
    def get_direction(self, t):
        """
        获取方向
        """
        return self.mode.get_direction(t)
    def get_speed(self, t):
        """
        获取速度
        """
        return self.mode.get_speed(t)
    def get_heading(self, t):
        """
        获取航向
        """
        return self.mode.get_heading(t)
    def set_threaten_level(self, level):
        """
        设置威胁级别
        """
        self.mode.set_threaten_level(level)
    def get_threaten_level(self, t):
        """
        获取危险等级
        :param t: 时间
        :return: 危险等级
        """
        return self.mode.get_threaten_level(t)
    def get_type(self):
        """
        获取攻击方的武器类型
        :return: utils.Utils.Types
        """
        return self.type
    def get_is_alive(self):
        """
        返回是否存活
        :return: bool
        """
        return self.mode.get_is_alive()
    def destroy(self):
        """
        摧毁目标
        """
        # TODO: to finish
        pass
    def get_mode_name(self):
        """
        获取模型名字
        :return: string
        """
        return self.mode.get_mode_name()
