from collections import namedtuple
import numpy

VentLine = namedtuple('VentLine', ['point1', 'point2'])

def parse(input_lines: list[str]) -> list[VentLine]:
    vent_lines = []

    for line in input_lines:
        points = line.split(" -> ")
        point1 = points[0].split(',')
        point2 = points[1].split(',')
        vent_lines.append(VentLine((int(point1[0]), int(point1[1])), (int(point2[0]), int(point2[1]))))
    
    return vent_lines


def filter_out_diagonal_lines(vent_lines: list[VentLine]) -> list[VentLine]:
    straight_lines = []

    for line in vent_lines:
        if is_straight(line):
            straight_lines.append(line)
    
    return straight_lines


def is_straight(vent_line: VentLine) -> bool:
    return vent_line.point1[0] == vent_line.point2[0] or vent_line.point1[1] == vent_line.point2[1]


def count_overlaps(vent_lines: list[VentLine]) -> int:
    max_x = find_max_x(vent_lines)
    max_y = find_max_y(vent_lines)
    vents_map = numpy.zeros(shape=(max_x+1, max_y+1))

    for ventLine in vent_lines:
        point1 = ventLine.point1
        point2 = ventLine.point2

        if point1[0] != point2[0]:
            # horizontal
            index = min(point1[0], point2[0])
            while index <= max(point1[0], point2[0]):
                vents_map[index, point1[1]] += 1
                index += 1
        elif point1[1] != point2[1]:
            # vertical
            index = min(point1[1], point2[1])
            while index <= max(point1[1], point2[1]):
                vents_map[point1[0], index] += 1
                index += 1

    overlaps = 0
    for i in range(max_x+1):
        for j in range(max_y+1):
            map_xy = vents_map[i, j]
            if vents_map[i, j] > 1:
                overlaps += 1

    return overlaps


def find_max_x(vent_lines: list[VentLine]) -> int:
    max_x = 0

    for ventLine in vent_lines:
        if ventLine.point1[0] > max_x:
            max_x = ventLine.point1[0]
        elif ventLine.point2[0] > max_x:
            max_x = ventLine.point2[0]
    
    return max_x


def find_max_y(vent_lines: list[VentLine]) -> int:
    max_y = 0

    for ventLine in vent_lines:
        if ventLine.point1[1] > max_y:
            max_y = ventLine.point1[1]
        elif ventLine.point2[1] > max_y:
            max_y = ventLine.point2[1]
    
    return max_y


def count_overlaps_for_straight_vents() -> int:
    with open('input', 'r') as file:
        input_lines = file.readlines()
        vent_lines = parse(input_lines)
        vent_lines = filter_out_diagonal_lines(vent_lines)
        result = count_overlaps(vent_lines)
        file.close()

        return result