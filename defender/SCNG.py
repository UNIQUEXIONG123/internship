# "SCNG": 小口径舰炮(Small caliber naval gun)
from defender.Defender import Defender


class SCNG(Defender):
    def __init__(self, speed, angular_velocity):
        super().__init__(speed)
        self.angular_velocity = angular_velocity

    def get_speed(self):
        return self.speed

    def get_angular_velocity(self):
        return self.angular_velocity