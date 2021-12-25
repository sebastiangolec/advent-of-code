from os import closerange
from crabs import Crabs


with open('input', 'r') as file:
    crabs = Crabs(file.readline())
    print(crabs.find_best_position())
    file.close()