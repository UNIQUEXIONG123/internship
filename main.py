from typing import List, Tuple

import numpy as np

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

    now_time = 0
    flag = True
    while(len(prepare_list)!=0 or len(destory_list)!=0):
        print(f'此时一共有{len(prepare_list)}个攻击武器')
        if len(prepare_list)!=0:
            prepare_list.sort(key=lambda item: item.get_threaten_level(now_time), reverse=True)

            print(f'在' + str(now_time) + f'时刻 为发现的敌方目标分配防御武器')
            dur_time = 0

            for item in prepare_list:
                if isinstance(item, Attacker):
                    print(item.get_type(), item.get_mode_name(), item.get_distance(now_time), item.get_threaten_level(now_time))
                if len(allocate_list)!=0:
                    temp_time,except_time = defender_generator.launch_defenders(item,now_time)
                    dur_time = max(dur_time,temp_time)
                    #移除该导弹
                    defender_generator.add_destroy_list(item ,except_time+now_time)
                    # launch_list.append(item)
                if len(allocate_list)==0:
                    print(f'缺失弹药，无法分配,我方目标被摧毁')
                    flag = False
                    break
            if flag == False:
                break
            now_time = dur_time + now_time
            prepare_list = []
            print(f'在'+str(now_time)+f'时刻，武器分配完成')
            print(f'此时一共分配了{len(destory_list)}个攻击武器')
        if len(destory_list)!=0:
            destory_item = destory_list.pop()
            now_time = destory_item[1]
            if now_time == float('inf'):
                continue
            print(f'判断在 {now_time:.7f} 时刻，目标对象 {destory_item[0].get_type()} 是否被摧毁')
            probability_of_one = 0.6
                # 生成[0, 1)之间的随机数
            random_number = np.random.rand()
                # 根据概率映射到0或1
            if random_number < probability_of_one:
                random_number = 1
            else:
                random_number = 0
            # 确保随机数在0和1之
            # # !TODO:判断是否被摧毁
            if random_number == 0:
                print(f'未能够被摧毁，将重新分配')
                prepare_list = []
                # defender_generator.add_prepare_list(destory_item[0])
                prepare_list.append(destory_item[0])
            else:

                print(f'已经完成了摧毁')
    if flag == True:
        print(f'成功进行了防御')


