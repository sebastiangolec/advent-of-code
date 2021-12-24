from lantern_fish import LanternFish


def simualate():
    with open('input', 'r') as file:
        lantern_fish = LanternFish(file.readline())
        print(len(lantern_fish.simulate(80)))
        file.close()

simualate()