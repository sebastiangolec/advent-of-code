class Crabs:
    initial_state = []
    max_index: int
    exp_cost_table = []

    def __init__(self, input_str: str):
        initial_state = [int(item) for item in input_str.split(',')]
        self.max_index = max(initial_state)
        self.initial_state = [0] * (self.max_index + 1)
        self.exp_cost_table = [0] * (self.max_index + 1)

        for crab in initial_state:
            self.initial_state[crab] += 1

    
    def calculate_linear_cost(self, position: int) -> int:
        cost = 0

        for i in range(0, len(self.initial_state)):
            if i > position:
                cost += self.initial_state[i] * (i - position)
            else:
                cost += self.initial_state[i] * (position - i)

        return cost
    

    def calculate_exponential_cost(self, position: int) -> int:
        cost = 0

        for i in range(0, len(self.initial_state)):
            if i >= position:
                distance = i - position
            else:
                distance = position - i

            cost += self.initial_state[i] * self.calculate_cost(distance)

        return cost


    def find_best_position_simple(self) -> tuple:
        results = [0] * (self.max_index + 1)

        for i in range(0, self.max_index+1):
            results[i] = self.calculate_linear_cost(i)
        
        min_cost = min(results)

        return (results.index(min_cost), min_cost)


    # try to reimplement this becasue finding solution took some time
    def find_best_posisiton_exponential(self) -> tuple:
        results = [0] * (self.max_index + 1)

        for i in range(0, self.max_index+1):
            results[i] = self.calculate_exponential_cost(i)
        
        min_cost = min(results)

        return (results.index(min_cost), min_cost)


    def calculate_cost(self, number: int):
        cost = 0

        if self.exp_cost_table[number] != 0:
            cost = self.exp_cost_table[number]
        else:
            for i in range(1, number+1):
                cost += i
                
            self.exp_cost_table[number] = cost

        return cost