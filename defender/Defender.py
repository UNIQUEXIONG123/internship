class Defender:
    # 防御武器飞行的速度
    def __init__(self, speed,noise):
        self.speed = speed
        self.noise = noise
    def get_speed(self):
        return self.speed
    def get_noise(self):
        return self.noise
