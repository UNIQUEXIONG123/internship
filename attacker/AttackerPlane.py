from abc import ABC, abstractmethod
from attacker.Attacker import Attacker
from attacker.mode.PlaneMode import DefaultPlaneMode


class AttackerPlane(Attacker, ABC):

    def __init__(self):
        super().__init__()
        self.mode = DefaultPlaneMode()

    # 获取干扰弹的数量
    def get_countermeasure(self, t):
        return self.mode.get_countermeasure(t)
