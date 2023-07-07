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

    def __init__(self, hypersonic_mode):
        super().__init__()
        self.mode = hypersonic_mode_dic[hypersonic_mode]()
