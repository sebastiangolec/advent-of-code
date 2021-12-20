import numpy
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


@dataclass
class VentLine:
    point1: Point
    point2: Point


    @classmethod
    def fromLine(cls, line: str):
        coords = line.split(" -> ")
        coord1 = coords[0].split(',')
        coord2 = coords[1].split(',')
        point1 = Point(int(coord1[0]), int(coord1[1]))
        point2 = Point(int(coord2[0]), int(coord2[1]))

        return VentLine(point1, point2)


    def is_horizontal(self) -> bool:
        return self.point1.x != self.point2.x


    def is_vertical(self) -> bool:
        return self.point1.y != self.point2.y


    def is_straight(self) -> bool:
        return self.point1.x == self.point2.x or self.point1.y == self.point2.y


def parse(input_lines: list[str]) -> list[VentLine]:
    vent_lines = []

    for line in input_lines:
        vent_lines.append(VentLine.fromLine(line))
    
    return vent_lines


def filter_out_diagonal_lines(vent_lines: list[VentLine]) -> list[VentLine]:
    straight_lines = []

    for line in vent_lines:
        if line.is_straight():
            straight_lines.append(line)
    
    return straight_lines


def map_vent_lines(vent_lines: list[VentLine]) -> numpy.ndarray:
    vents_map = numpy.zeros(shape=(1000, 1000))

    for vent_line in vent_lines:
        point1 = vent_line.point1
        point2 = vent_line.point2

        if vent_line.is_horizontal():
            index = min(point1.x, point2.x)
            while index <= max(point1.x, point2.x):
                vents_map[index, point1.y] += 1
                index += 1
        elif vent_line.is_vertical():
            index = min(point1.y, point2.y)
            while index <= max(point1.y, point2.y):
                vents_map[point1.x, index] += 1
                index += 1
    
    return vents_map


def count_overlaps(vents_map: numpy.ndarray) -> int:
    overlaps = 0

    for i in range(1000):
        for j in range(1000):
            if vents_map[i, j] > 1:
                overlaps += 1

    return overlaps


def count_overlaps_for_straight_vents() -> int:
    with open('input', 'r') as file:
        vent_lines = parse(file.readlines())
        file.close()

        vent_lines = filter_out_diagonal_lines(vent_lines)
        vents_map = map_vent_lines(vent_lines)
        result = count_overlaps(vents_map)

        return result