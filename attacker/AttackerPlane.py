from abc import ABC, abstractmethod
from attacker.Attacker import Attacker


class AttackerPlane(Attacker, ABC):

    def __init__(self):
        super().__init__()

    # 获取干扰弹的数量
    @abstractmethod
    def get_countermeasure(self):
        pass
