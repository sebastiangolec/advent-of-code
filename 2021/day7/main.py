from os import closerange
from crabs import Crabs


with open('input', 'r') as file:
    crabs = Crabs(file.readline())
    print(crabs.find_best_position_simple())
    print(crabs.find_best_posisiton_exponential())
    file.close()