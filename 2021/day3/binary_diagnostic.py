'''--- Day 3: Binary Diagnostic ---'''
path = "2021/day3/input"

def calculatePowerConsumption(input) -> int:
    gammaRate = determineGammaRate(input)
    deltaRate = determineDeltaRate(input)

    return gammaRate * deltaRate

def determineGammaRate(input: list[str]) -> int:
    gammaRateBinary: str = ''
    i = 0
    lineLength = len(input[0].rstrip())

    while i < lineLength:
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
    lineLength = len(input[0].rstrip())

    while i < lineLength:
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

def calculateLifeSupportRating(input: list[str]) -> int:
    oxygenGeneratorRating = determineOxygenGeneratorRating(input.copy())
    co2ScrubberRating = determineCo2ScrubberRating(input.copy())

    return oxygenGeneratorRating * co2ScrubberRating

def determineOxygenGeneratorRating(input: list[str]) -> int:
    oxygenGeneratorRatingBinary = ''
    i = 0
    lineLength = len(input[0].rstrip())

    while i < lineLength:
        bit = determineMostCommonBit(i, input)
        oxygenGeneratorRatingBinary += bit
        input = filterLinesWithBit(i, bit, input)
        i += 1

        if(len(input) == 1):
            return int(input[0], 2)

    return int(oxygenGeneratorRatingBinary, 2)

def determineCo2ScrubberRating(input: list[str]) -> int:
    co2ScrubberRatingBinary = ''
    i = 0
    lineLength = len(input[0].rstrip())

    while i < lineLength:
        bit = determineLeastCommonBit(i, input)
        co2ScrubberRatingBinary += bit
        input = filterLinesWithBit(i, bit, input)
        i += 1

        if(len(input) == 1):
            return int(input[0], 2)

    return int(co2ScrubberRatingBinary, 2)

def filterLinesWithBit(index: int, bit: str, input: list[str]):
    newInput = []
    for line in input:
        if line[index] == bit:
            newInput.append(line)
    
    return newInput


powerConsumption = calculatePowerConsumption(open(path, 'r').readlines())
print(powerConsumption)

lifeSupportRating = calculateLifeSupportRating(open(path, 'r').readlines())
print(lifeSupportRating)