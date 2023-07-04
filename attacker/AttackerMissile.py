from abc import ABC
from attacker.Attacker import Attacker


class AttackerMissile(Attacker, ABC):

    def __init__(self, start_distance, start_height, start_direction, start_speed, start_heading, start_time,
                 max_height, min_height, max_speed, min_speed, threaten_level, is_alive):
        super().__init__(start_distance, start_height, start_direction, start_speed, start_heading, start_time,
                         max_height, min_height, max_speed, min_speed, threaten_level, is_alive)