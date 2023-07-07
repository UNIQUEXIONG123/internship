from attacker.AttackerPlane import AttackerPlane
from attacker.plane.PlaneMode import plane_mode_dic


class Fighter(AttackerPlane):
    def set_threaten_level(self, level):
        self.mode.set_threaten_level(level)

    def __init__(self):
        super().__init__()
        self.mode = plane_mode_dic[2]()

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

    def get_countermeasure(self):
        return self.mode.get_countermeasure()
