from defender.Defender import Defender

class SRAD(Defender):
    def __init__(self, speed, delay):
        super().__init__(speed,delay)

    def get_speed(self):
        return self.speed

    def get_delay(self):
        return self.delay

