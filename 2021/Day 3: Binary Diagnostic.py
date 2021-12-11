path = "/Users/sebastiangolec/AdventOfCode/2021/Day 3 input"

def calculatePowerConsumption(input) -> int:
    gammaRate = determineGammaRate(input)
    deltaRate = determineDeltaRate(input)

    return gammaRate * deltaRate

def determineGammaRate(input: list[str]) -> int:
    gammaRateBinary: str = ''
    i = 0

    while i < len(input[0].rstrip()):
        gammaRateBinary += determineMostCommonBit(i, input)
        i += 1

    return int(gammaRateBinary, 2)

def determineMostCommonBit(index: int, input: list[str]) -> str:
    zeroes = 0
    ones = 0

    for line in input:
        bit = line[index]
        match bit:
            case '0':
                zeroes += 1
            case '1':
                ones += 1
    
    if zeroes > ones:
        return '0'
    else:
        return '1'

def determineDeltaRate(input: list[str]) -> int:
    deltaRateBinary: str = ''
    i = 0

    while i < len(input[0].rstrip()):
        deltaRateBinary += determineLeastCommonBit(i, input)
        i += 1

    return int(deltaRateBinary, 2)

def determineLeastCommonBit(index: int, input: list[str]) -> str:
    zeroes = 0
    ones = 0

    for line in input:
        bit = line[index]
        match bit:
            case '0':
                zeroes += 1
            case '1':
                ones += 1
    
    if zeroes > ones:
        return '1'
    else:
        return '0'
            

powerConsumption = calculatePowerConsumption(open(path, 'r').readlines())
print(powerConsumption)