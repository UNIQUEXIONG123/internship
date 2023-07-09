from attacker.AttackerPlane import AttackerPlane
from attacker.mode.PlaneMode import plane_mode_dic
from utils.Utils import AttackerTypes


class Helicopter(AttackerPlane):

    def __init__(self):
        super().__init__()
        self.type = AttackerTypes.HELICOPTER
        self.mode = plane_mode_dic[3]()
