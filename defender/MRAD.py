# "MRAD": 中距离防空导弹(Medium-range air defense missile)
from defender.Defender import Defender

class MRAD(Defender):
    def __init__(self, speed, delay):
        super().__init__(speed,delay)
        self.delay = delay

    def get_speed(self):
        return self.speed

    def get_delay(self):
        return self.delay
