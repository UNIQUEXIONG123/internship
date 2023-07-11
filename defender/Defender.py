from abc import ABC

from utils.Utils import DefenderTypes
class Defender(ABC):

    # 防御武器的延迟时间
    def __init__(self,speed,delay):
        self.type = DefenderTypes.DEFAULT_TYPE
        self.speed = speed
        self.delay = delay

    def get_speed(self):
        return self.speed

    def get_delay(self):
        return self.delay

    def get_type(self):
        return self.type

