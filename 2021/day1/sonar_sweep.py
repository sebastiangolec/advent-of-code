'''--- Day 1: Sonar Sweep ---'''
path = "2021/day1/input"

# 1 star
def calculateDepressions(input):
    counter = 0
    base = int(input[0])
    i = 1

    while i < len(input):
        scan = int(input[i])

        if base < scan:
            counter = counter + 1

        base = scan
        i = i+1

    return counter

# 2 stars
def calculateDepressionSums(input):
    counter = 0
    baseSum = int(input[0]) + int(input[1]) + int(input[2])
    i = 1

    while i < len(input) - 2:
        scanSum = int(input[i]) + int(input[i+1]) + int(input[i+2])
        if baseSum < scanSum:
            counter = counter + 1
        baseSum = scanSum
        i = i+1
    
    return counter

print(calculateDepressions(open(path, 'r').readlines()))
print(calculateDepressionSums(open(path, 'r').readlines()))