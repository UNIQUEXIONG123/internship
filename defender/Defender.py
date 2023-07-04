class Defender:
    # 防御武器飞行的速度
    # 防御武器的延迟时间
    def __init__(self, speed,delay):
        self.speed = speed
        self.delay = delay
    def get_speed(self):
        return self.speed
    def get_delay(self):
        return self.delay
