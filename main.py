import attacker.missile.Subsonic as subsonic
import attacker.missile.MissileMode as mode
if __name__ == '__main__':
    subsonic = subsonic.Subsonic(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, True, mode.SubsonicMode.STRAIGHT_LINE)
    print(subsonic.is_alive)
