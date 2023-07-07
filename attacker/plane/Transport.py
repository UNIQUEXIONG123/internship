from attacker.AttackerPlane import AttackerPlane
from attacker.plane.PlaneMode import plane_mode_dic


class Transport(AttackerPlane):

    def get_threaten_level(self):
        return self.mode.threaten_level

    def set_threaten_level(self, level):
        self.mode.set_threaten_level(level)

    def get_distance(self, t):
        return self.mode.get_distance(t)

    def get_height(self, t):
        return self.mode.get_height(t)

    def get_direction(self, t):
        return self.mode.get_direction(t)

    def get_speed(self, t):
        return self.mode.get_speed(t)

    def get_heading(self, t):
        return self.mode.get_heading(t)

    def get_countermeasure(self):
        return self.mode.get_countermeasure()

    def __init__(self):
        super().__init__()
        self.mode = plane_mode_dic[4]()
