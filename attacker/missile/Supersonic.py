from attacker.AttackerMissile import AttackerMissile


class Supersonic(AttackerMissile):

    def get_distance(self):
        pass

    def get_height(self):
        pass

    def get_direction(self):
        pass

    def get_speed(self):
        pass

    def get_heading(self):
        pass

    def get_countermeasure(self):
        pass

    def __init__(self, start_distance, start_height, start_direction, start_speed, start_heading, start_time,
                 max_height, min_height, max_speed, min_speed, threaten_level, is_alive, supersonic_mode):
        super().__init__(start_distance, start_height, start_direction, start_speed, start_heading,
                         start_time,
                         max_height, min_height, max_speed, min_speed, threaten_level, is_alive)
        self.mode = supersonic_mode
