from attacker.AttackerPlane import AttackerPlane
from attacker.plane.PlaneMode import plane_mode_dic


class Transport(AttackerPlane):

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

    def __init__(self):
        super().__init__()
        self.mode = plane_mode_dic[4]()
