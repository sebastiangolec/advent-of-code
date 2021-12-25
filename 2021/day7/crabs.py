class Crabs:
    initial_state = []
    max_index: int

    def __init__(self, input_str: str):
        initial_state = [int(item) for item in input_str.split(',')]
        self.max_index = max(initial_state)
        self.initial_state = [0] * (self.max_index + 1)

        for crab in initial_state:
            self.initial_state[crab] += 1

    
    def calculate_cost(self, position: int) -> int:
        cost = 0

        for i in range(0, len(self.initial_state)):
            if i > position:
                cost += self.initial_state[i] * (i - position)
            else:
                cost += self.initial_state[i] * (position - i)

        return cost


    def find_best_position(self) -> tuple:
        results = [0] * (self.max_index + 1)

        for i in range(0, self.max_index+1):
            results[i] = self.calculate_cost(i)
        
        min_cost = min(results)

        return (results.index(min_cost), min_cost)