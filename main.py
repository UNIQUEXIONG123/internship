from generator.AttackerGenerator import attacker_generator
from generator.DefenderGenerator import defender_generator

if __name__ == '__main__':
    attacker_generator.generate()
    for item in defender_generator.prepared_list:
        print(item)
