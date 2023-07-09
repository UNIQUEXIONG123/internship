from attacker.AttackerMissile import AttackerMissile
from attacker.mode.MissileMode import supersonic_mode_dic
from utils.Utils import AttackerTypes


class Supersonic(AttackerMissile):

    def __init__(self, supersonic_mode):
        super().__init__()
        self.type = AttackerTypes.SUPERSONIC
        self.mode = supersonic_mode_dic[supersonic_mode]()
