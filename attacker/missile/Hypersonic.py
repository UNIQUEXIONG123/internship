from attacker.AttackerMissile import AttackerMissile
from attacker.mode.MissileMode import hypersonic_mode_dic
from utils.Utils import AttackerTypes


class Hypersonic(AttackerMissile):

    def __init__(self, hypersonic_mode):
        super().__init__()
        self.type = AttackerTypes.HYPERSONIC
        self.mode = hypersonic_mode_dic[hypersonic_mode]()
