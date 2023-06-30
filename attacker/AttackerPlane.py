from abc import ABC, abstractmethod
from attacker.Attacker import Attacker


class AttackerPlane(Attacker, ABC):

    def __init__(self, start_distance, start_height, start_direction, start_speed, start_heading, start_time,
                 max_height, min_height, max_speed, min_speed, threaten_level, is_alive, countermeasure):
        super().__init__(start_distance, start_height, start_direction, start_speed, start_heading, start_time,
                         max_height, min_height, max_speed, min_speed, threaten_level, is_alive)
        self.countermeasure = countermeasure

    # 获取干扰弹的数量
    @abstractmethod
    def get_countermeasure(self):
        pass
