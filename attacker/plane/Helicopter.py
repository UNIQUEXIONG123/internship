from attacker.AttackerPlane import AttackerPlane
from attacker.plane.PlaneMode import helicopter_mode_dic


class Helicopter(AttackerPlane):

    def get_distance(self):
        return self.mode.get_distance()

    def get_height(self):
        return self.mode.get_height()

    def get_direction(self):
        return self.mode.get_direction()

    def get_speed(self):
        return self.mode.get_speed()

    def get_heading(self):
        return self.mode.get_heading()

    def get_countermeasure(self):
        return self.mode.get_countermeasure()

    def __init__(self, start_distance, start_height, start_direction, start_speed, start_heading, start_time,
                 max_height, min_height, max_speed, min_speed, threaten_level, is_alive, countermeasure,
                 helicopter_mode):
        super().__init__(start_distance, start_height, start_direction, start_speed, start_heading,
                         start_time,
                         max_height, min_height, max_speed, min_speed, threaten_level, is_alive, countermeasure)
        self.mode = helicopter_mode_dic[helicopter_mode]()

    class HelicopterMode:
        STRAIGHT_LINE = 1  # 直线飞行模式
        LOW_LEVEL = 2  # 低空飞行模式
        SOARING = 3  # 栈道飞行
