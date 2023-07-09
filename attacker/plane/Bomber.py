from attacker.AttackerPlane import AttackerPlane
from attacker.mode.PlaneMode import plane_mode_dic
from utils.Utils import AttackerTypes


class Bomber(AttackerPlane):

    def __init__(self):
        super().__init__()
        self.type = AttackerTypes.BOMBER
        self.mode = plane_mode_dic[1]()
