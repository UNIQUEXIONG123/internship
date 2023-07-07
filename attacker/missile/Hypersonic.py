from attacker.AttackerMissile import AttackerMissile
from attacker.missile.MissileMode import hypersonic_mode_dic


class Hypersonic(AttackerMissile):

    def set_threaten_level(self, level):
        pass

    def get_distance(self, t):
        return self.mode.get_distance(t)

    def get_height(self, t):
        return self.mode.get_height(t)

    def get_direction(self, t):
        return self.mode.get_direction(t)

    def get_speed(self, t):
        return self.mode.get_speed()

    def get_heading(self, t):
        return self.mode.get_heading()

    def __init__(self, hypersonic_mode):
        super().__init__()
        self.mode = hypersonic_mode_dic[hypersonic_mode]()
