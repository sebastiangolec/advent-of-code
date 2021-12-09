path = '/Users/sebastiangolec/AdventOfCode/2021/Day 2 input'

def calculatePosition(input):
    distance = 0
    depth = 0

    while len(input) > 0:
        command = input.pop().split(" ")
        match command[0]:
            case 'forward':
                distance += int(command[1])
            case 'up':
                depth -= int(command[1])
            case 'down':
                depth += int(command[1])

    return distance, depth


input_file = open(path, 'r')
input = input_file.readlines()
position = calculatePosition(input)

print(position[0], position[1])
print(int(position[0]) * int (position[1]))