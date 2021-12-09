path = '/Users/sebastiangolec/AdventOfCode/2021/Day 1 input'

input_file = open(path, 'r')
counter = 0

input = input_file.readlines()
baseSum = int(input[0]) + int(input[1]) + int(input[2])
i = 1

while i < len(input) - 2:
    scanSum = int(input[i]) + int(input[i+1]) + int(input[i+2])
    if baseSum < scanSum:
        counter = counter + 1
    baseSum = scanSum
    i = i+1

print(counter)