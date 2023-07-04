# "SRAD"： 近距离防空导弹(Small-range air defense missile)
from defender.Defender import Defender


class SRAD(Defender):

    def __init__(self, speed, delay):
        super().__init__(speed, delay)
        self.delay = delay

    def get_speed(self):
        return self.speed
