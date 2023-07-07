from abc import ABC
from attacker.Attacker import Attacker


class AttackerMissile(Attacker, ABC):

    def __init__(self):
        super().__init__()
