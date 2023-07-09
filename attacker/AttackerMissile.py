from abc import ABC
from attacker.Attacker import Attacker
from attacker.mode.MissileMode import DefaultMissileMode


class AttackerMissile(Attacker, ABC):

    def __init__(self):
        super().__init__()
        self.mode = DefaultMissileMode()
