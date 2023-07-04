from defender.Defender import Defender

class MC(Defender):
    # 导弹车认为他发射的时候的初速度为0
    def __init__(self, speed, delay, angular_velocity):
        super().__init__(speed,delay)
        self.angular_velocity = angular_velocity

    def get_speed(self):
        return self.speed

    def get_delay(self):
        return self.delay

    def get_angular_velocity(self):
        return self.angular_velocity
