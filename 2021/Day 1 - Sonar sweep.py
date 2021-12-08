path = '/Users/sebastiangolec/AdventOfCode/2021/input'

input_file = open(path, 'r')
counter = 0

input = input_file.readlines()
base = int(input[0])
i = 1

while i < len(input):
    scan = int(input[i])
    if base < scan:
        counter = counter + 1
    base = scan
    i = i+1

print(counter)