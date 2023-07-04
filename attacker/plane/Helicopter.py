from attacker.AttackerPlane import AttackerPlane


class Helicopter(AttackerPlane):

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

    def __init__(self, start_distance, start_height, start_direction, start_speed, start_heading, start_time,
                 max_height, min_height, max_speed, min_speed, threaten_level, is_alive, countermeasure,
                 helicopter_mode):
        super().__init__(start_distance, start_height, start_direction, start_speed, start_heading,
                         start_time,
                         max_height, min_height, max_speed, min_speed, threaten_level, is_alive, countermeasure)
        self.mode = helicopter_mode

    class HelicopterMode:
        STRAIGHT_LINE = 1  # 直线飞行模式
        LOW_LEVEL = 3  # 低空飞行模式
        SOARING = 4  # 栈道飞行