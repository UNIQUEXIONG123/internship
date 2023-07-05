from attacker.AttackerMissile import AttackerMissile
from attacker.missile.MissileMode import hypersonic_mode_dic


class Hypersonic(AttackerMissile):

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

    def __init__(self, start_distance, start_height, start_direction, start_speed, start_heading, start_time,
                 max_height, min_height, max_speed, min_speed, threaten_level, is_alive, hypersonic_mode):
        super().__init__(start_distance, start_height, start_direction, start_speed, start_heading,
                         start_time,
                         max_height, min_height, max_speed, min_speed, threaten_level, is_alive)
        self.mode = hypersonic_mode_dic[hypersonic_mode]()
