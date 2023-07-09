from attacker.AttackerMissile import AttackerMissile
from attacker.mode.MissileMode import subsonic_mode_dic
from utils.Utils import AttackerTypes


class Subsonic(AttackerMissile):

    def __init__(self, subsonic_mode):
        super().__init__()
        self.type = AttackerTypes.SUBSONIC
        self.mode = subsonic_mode_dic[subsonic_mode]()
