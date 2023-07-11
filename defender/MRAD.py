# "MRAD": 中距离防空导弹(Medium-range air defense missile)
from defender.Defender import Defender
from utils.Utils import DefenderTypes

class MRAD(Defender):
    def __init__(self, speed, delay):
        super().__init__(speed, delay)
        self.type = DefenderTypes.MRAD

    def get_speed(self):
        return self.speed

    def get_delay(self):
        return self.delay

    def get_type(self):
        return self.type
