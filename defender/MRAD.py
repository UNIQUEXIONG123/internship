from defender.Defender import Defender

class MRAD(Defender):
    def __init__(self, speed, delay):
        super().__init__(speed)
        self.delay = delay

    def get_speed(self):
        return self.speed

    def get_delay(self):
        return self.delay
