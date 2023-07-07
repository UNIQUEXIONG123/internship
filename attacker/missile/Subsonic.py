from attacker.AttackerMissile import AttackerMissile
from attacker.missile.MissileMode import subsonic_mode_dic


class Subsonic(AttackerMissile):

    def set_threaten_level(self, level):
        pass

    def get_distance(self, t):
        return self.mode.get_distance()

    def get_height(self, t):
        return self.mode.get_height()

    def get_direction(self, t):
        return self.mode.get_direction()

    def get_speed(self, t):
        return self.mode.get_speed()

    def get_heading(self, t):
        return self.mode.get_heading()

    def __init__(self, subsonic_mode):
        super().__init__()
        self.mode = subsonic_mode_dic[subsonic_mode]()
