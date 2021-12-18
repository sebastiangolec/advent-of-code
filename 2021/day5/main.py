'''--- Day 5: Hydrothermal Venture ---'''

from collections import namedtuple
import numpy

VentLine = namedtuple('VentLine', ['point1', 'point2'])

def parse(input: list[str]) -> list[VentLine]:
    ventLines = []

    for line in input:
        points = line.split(" -> ")
        point1 = points[0].split(',')
        point2 = points[1].split(',')
        ventLines.append(VentLine((int(point1[0]), int(point1[1])), (int(point2[0]), int(point2[1]))))
    
    return ventLines

def filterOutDiagonalLines(ventLines: list[VentLine]) -> list[VentLine]:
    straightLines = []

    for line in ventLines:
        if isStraight(line):
            straightLines.append(line)
    
    return straightLines

def isStraight(ventLine: VentLine) -> bool:
    return ventLine.point1[0] == ventLine.point2[0] or ventLine.point1[1] == ventLine.point2[1]

def countOverlaps(ventLines: list[VentLine]) -> int:
    maxX = findMaxX(ventLines)
    maxY = findMaxY(ventLines)
    map = numpy.zeros(shape=(maxX+1, maxY+1))

    for ventLine in ventLines:
        point1 = ventLine.point1
        point2 = ventLine.point2

        if point1[0] != point2[0]:
            # horizontal
            index = min(point1[0], point2[0])
            while index <= max(point1[0], point2[0]):
                map[index, point1[1]] += 1
                index += 1
        elif point1[1] != point2[0]:
            # vertical
            index = min(point1[1], point2[1])
            while index <= max(point1[1], point2[1]):
                map[point1[0], index] += 1
                index += 1

    overlaps = 0
    for i in range(maxX+1):
        for j in range(maxY+1):
            mapXY = map[i,j]
            if map[i, j] > 1:
                overlaps += 1

    return overlaps

def findMaxX(ventLines: list[VentLine]) -> int:
    maxX = 0

    for ventLine in ventLines:
        if ventLine.point1[0] > maxX:
            maxX = ventLine.point1[0]
        elif ventLine.point2[0] > maxX:
            maxX = ventLine.point2[0]
    
    return maxX

def findMaxY(ventLines: list[VentLine]) -> int:
    maxY = 0

    for ventLine in ventLines:
        if ventLine.point1[1] > maxY:
            maxY = ventLine.point1[1]
        elif ventLine.point2[1] > maxY:
            maxY = ventLine.point2[1]
    
    return maxY

def main():
    input = open('2021/day5/input', 'r').readlines()
    ventLines = parse(input)
    ventLines = filterOutDiagonalLines(ventLines)
    result = countOverlaps(ventLines)
    print(result)

main()