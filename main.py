from typing import List, Tuple

from generator.AttackerGenerator import attacker_generator
from generator.DefenderGenerator import defender_generator
from attacker.Attacker import Attacker
from defender.Defender import Defender

if __name__ == '__main__':
    attacker_generator.generate()
    prepare_list: List[Attacker] = defender_generator.get_prepare_list()
    allocate_list : List[Defender] = defender_generator.get_allocate_list()
    # launch_list : List[Attacker] = defender_generator.get_launch_list()
    # estimate_list: List[int] = defender_generator.get_estimate_list()
    destory_list: List[Tuple[Attacker,int]] = defender_generator.get_destroy_list()
    print('length', len(prepare_list))
    print('length', len(allocate_list))
    # prepare_list.sort(key=lambda item:item.get_threaten_level(0),reverse=True)
    past_time = 0
    now_time = 0
    while(len(prepare_list)!=0 or len(destory_list)!=0):

        if len(prepare_list)!=0:
            prepare_list.sort(key=lambda item: item.get_threaten_level(0), reverse=True)
            print(f'在' + str(now_time) + f'时刻 为发现的敌方目标分配防御武器')
            dur_time = 0
            for item in prepare_list:
                if isinstance(item, Attacker):
                    print(item.get_type(), item.get_mode_name(), item.get_distance(now_time), item.get_threaten_level(now_time))
                if len(allocate_list)!=0:
                    temp_time,except_time = defender_generator.launch_defenders(item,now_time)
                    dur_time = max(dur_time,temp_time)
                    #移除该导弹
                    prepare_list.pop()
                    defender_generator.add_destroy_list(item ,except_time+now_time)
                    # launch_list.append(item)
                if len(allocate_list)==0:
                    print(f'缺失弹药，无法分配')
            now_time = dur_time + now_time
            print(f'在'+str(now_time)+f'时刻，武器分配完成')
        if len(destory_list)!=0:
            destory_item = destory_list.pop()
            now_time = destory_item[1]
            print(f'判断在'+str(now_time)+f'时刻，目标对象'+str(destory_item[0].get_type())+f'是否被摧毁')
            # if 被摧毁 :
            #
            # else :
            #     defender_generator.add_prepare_list(destory_item[0])

