class LanternFish():
    state: list[int]


    def __init__(self, initial_state: str):
        state = []
        for str in initial_state.split(","):
            state.append(int(str))
        
        self.state = state

    
    def simulate(self, days: int) -> list[int]:
        for day in range(0, days):
            new_state = []
            new_fishes = []

            for fish in self.state:
                if fish == 0:
                    new_state.append(6)
                    new_fishes.append(8)
                else:
                    new_state.append(fish - 1)
            
            for fish in new_fishes:
                new_state.append(fish)

            self.state = new_state
        
        return self.state