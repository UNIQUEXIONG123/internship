from typing import List


from generator.AttackerGenerator import attacker_generator
from generator.DefenderGenerator import defender_generator
from attacker.Attacker import Attacker
from defender.Defender import Defender

if __name__ == '__main__':
    attacker_generator.generate()
    prepare_list: List[Attacker] = defender_generator.get_prepare_list()
    print('length', len(prepare_list))
    for item in prepare_list:
        if isinstance(item, Attacker):
            print(item.get_type(), item.get_mode_name(), item.get_distance(0), item.get_threaten_level(0))
