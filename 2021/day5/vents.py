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
    

    def is_diagonal(self) -> bool:
        return self.point1.x != self.point2.x and self.point1.y != self.point2.y


    def is_straight(self) -> bool:
        return self.point1.x == self.point2.x or self.point1.y == self.point2.y

    
    def is_upstair(self) -> bool:
        return (self.point1.x > self.point2.x and self.point1.y > self.point2.y) or (self.point1.x < self.point2.x and self.point1.y < self.point2.y)
    

    def is_downstair(self) -> bool:
        return (self.point1.x > self.point2.x and self.point1.y < self.point2.y) or (self.point1.x < self.point2.x and self.point1.y > self.point2.y)


class VentsMap:
    vents_map: numpy.ndarray


    def __init__(self, vent_lines: list[VentLine]):
        self.vents_map = numpy.zeros(shape=(1000, 1000))
        self.map_vent_lines(vent_lines)       


    def map_vent_lines(self, vent_lines: list[VentLine]) -> numpy.ndarray:
        for vent_line in vent_lines:
            if vent_line.is_diagonal():
                self.map_diagonal_vent(vent_line)
            elif vent_line.is_horizontal():
                self.map_horizontal_vent(vent_line)
            elif vent_line.is_vertical():
                self.map_vertical_vent(vent_line)


    def map_diagonal_vent(self, vent_line: VentLine):
        if vent_line.is_upstair():
            self.map_upstairs_vent(vent_line)
        elif vent_line.is_downstair():
            self.map_downstairs_vent(vent_line)

    
    def map_upstairs_vent(self, vent_line: VentLine):
        base_point: Point
        distance: int

        if vent_line.point1.x < vent_line.point2.x:
            base_point = vent_line.point1
            distance = vent_line.point2.x - vent_line.point1.x
        else:
            base_point = vent_line.point2
            distance = vent_line.point1.x - vent_line.point2.x

        for i in range(0, distance+1):
            self.vents_map[base_point.x + i, base_point.y + i] += 1


    def map_downstairs_vent(self, vent_line: VentLine):
        base_point: Point
        distance: int

        if vent_line.point1.x < vent_line.point2.x:
            base_point = vent_line.point1
            distance = vent_line.point2.x - vent_line.point1.x
        else:
            base_point = vent_line.point2
            distance = vent_line.point1.x - vent_line.point2.x
        
        for i in range(0, distance+1):
            self.vents_map[base_point.x + i, base_point.y - i] += 1


    def map_horizontal_vent(self, vent_line: VentLine):
        index = min(vent_line.point1.x, vent_line.point2.x)

        while index <= max(vent_line.point1.x, vent_line.point2.x):
            self.vents_map[index, vent_line.point1.y] += 1
            index += 1


    def map_vertical_vent(self, vent_line: VentLine):
        index = min(vent_line.point1.y, vent_line.point2.y)

        while index <= max(vent_line.point1.y, vent_line.point2.y):
            self.vents_map[vent_line.point1.x, index] += 1
            index += 1


    def count_overlaps(self) -> int:
        overlaps = 0

        for i in range(1000):
            for j in range(1000):
                if self.vents_map[i, j] > 1:
                    overlaps += 1

        return overlaps


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


def count_overlaps_for_straight_vents() -> int:
    with open('input', 'r') as file:
        vent_lines = parse(file.readlines())
        file.close()

        vent_lines = filter_out_diagonal_lines(vent_lines)
        vents_map = VentsMap(vent_lines)
        
        return vents_map.count_overlaps()

def count_overlaps_for_all_vents() -> int:
    with open('input', 'r') as file:
        vent_lines = parse(file.readlines())
        file.close()
        vents_map = VentsMap(vent_lines)
        
        return vents_map.count_overlaps()