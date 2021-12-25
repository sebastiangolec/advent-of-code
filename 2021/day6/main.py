from lantern_fish import LanternFish


with open('input', 'r') as file:
    lantern_fish = LanternFish(file.readline())
    
    lantern_fish.simulate(80)
    print(lantern_fish.calculate_population())
    
    lantern_fish.simulate(256-80)
    print(lantern_fish.calculate_population())
    
    file.close()