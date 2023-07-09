from attacker.AttackerPlane import AttackerPlane
from attacker.mode.PlaneMode import plane_mode_dic
from utils.Utils import AttackerTypes


class Fighter(AttackerPlane):

    def __init__(self):
        super().__init__()
        self.type = AttackerTypes.FIGHTER
        self.mode = plane_mode_dic[2]()
