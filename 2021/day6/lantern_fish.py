class LanternFish():
    state: list[int]


    def __init__(self, initial_state: str):
        state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for str in initial_state.split(","):
            state[int(str)] += 1
        
        self.state = state

    
    def simulate(self, days: int):
        for day in range(0, days):
            new_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]

            new_state[8] += self.state[0] # new born fishses
            new_state[6] += self.state[0] # fishes that gave born today

            for i in range(0, 8):
                new_state[i] += self.state[i+1]

            self.state = new_state

    
    def calculate_population(self) -> int:
        population = 0

        for number in self.state:
            population += number

        return population