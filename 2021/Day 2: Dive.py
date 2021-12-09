path = "/Users/sebastiangolec/AdventOfCode/2021/Day 2 input"

def calculatePosition(input):
    distance = 0
    depth = 0

    while len(input) > 0:
        command = input.pop(0).split(" ")
        match command[0]:
            case 'forward':
                distance += int(command[1])
            case 'up':
                depth -= int(command[1])
            case 'down':
                depth += int(command[1])

    return distance, depth

def calculatePositionWithAim(input):
    distance = 0;
    depth = 0;
    aim = 0;

    while len(input) > 0:
        command = input.pop(0).split(" ")
        match command[0]:
            case 'forward':
                distance += int(command[1])
                depth += aim * int(command[1])
            case 'up':
                aim -= int(command[1])
            case 'down':
                aim += int(command[1])

    return distance, depth

input_file = open(path, 'r').readlines()
position = calculatePosition(open(path, 'r').readlines())
positionWithAim = calculatePositionWithAim(open(path, 'r').readlines())

print(position[0], position[1], int(position[0]) * int (position[1]))
print(positionWithAim[0], positionWithAim[1], int(positionWithAim[0]) * int (positionWithAim[1]))