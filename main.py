from typing import List


from generator.AttackerGenerator import attacker_generator
from generator.DefenderGenerator import defender_generator
from attacker.Attacker import Attacker
from defender.Defender import Defender

if __name__ == '__main__':
    attacker_generator.generate()
    prepare_list: List[Attacker] = defender_generator.get_prepare_list()
    allocate_list : List[Defender] = defender_generator.get_allocate_list()
    print('length', len(prepare_list))
    print('length', len(allocate_list))
    prepare_list.sort(key=lambda item:item.get_threaten_level(0),reverse=True)
    past_time = 0
    now_time = 0
    for item in prepare_list:
        past_time = now_time
        if isinstance(item, Attacker):
            print(item.get_type(), item.get_mode_name(), item.get_distance(0), item.get_threaten_level(0))
        if len(allocate_list)!=0:
            now_time = past_time + defender_generator.launch_defenders(item,past_time)
            print(past_time)

