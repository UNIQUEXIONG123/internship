from generator.EnvironmentEntity import attacker_generator
from attacker.plane.PlaneMode import get_threat_level

if __name__ == '__main__':
    # attacker_generator.generate()
    level = get_threat_level(4, "fighter")
    print(level)
