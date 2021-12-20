import unittest
import vents


def create_vent_line(x1: int, y1: int, x2: int, y2: int) -> vents.VentLine:
    point1 = vents.Point(x1, y1)
    point2 = vents.Point(x2, y2)

    return vents.VentLine(point1, point2)

class Test(unittest.TestCase):
    def test_parseInput(self):
        with open('test_input', 'r') as file:
            input_lines = file.readlines()
            result = vents.parse(input_lines)
            expected_result = [
                create_vent_line(0, 9, 5, 9),
                create_vent_line(8, 0, 0, 8),
                create_vent_line(9, 4, 3, 4),
                create_vent_line(2, 2, 2, 1),
                create_vent_line(7, 0, 7, 4),
                create_vent_line(6, 4, 2, 0),
                create_vent_line(0, 9, 2, 9),
                create_vent_line(3, 4, 1, 4),
                create_vent_line(0, 0, 8, 8),
                create_vent_line(5, 5, 8, 2)
            ]
            self.assertEqual(result, expected_result)
            file.close()


    def test_filterOutDiagonalLines(self):
        lines = [
            create_vent_line(0, 9, 5, 9),
            create_vent_line(8, 0, 0, 8),
            create_vent_line(9, 4, 3, 4),
            create_vent_line(2, 2, 2, 1),
            create_vent_line(7, 0, 7, 4),
            create_vent_line(6, 4, 2, 0),
            create_vent_line(0, 9, 2, 9),
            create_vent_line(3, 4, 1, 4),
            create_vent_line(0, 0, 8, 8),
            create_vent_line(5, 5, 8, 2)
        ]

        result = vents.filter_out_diagonal_lines(lines)

        expected_result = [
            create_vent_line(0, 9, 5, 9),
            create_vent_line(9, 4, 3, 4),
            create_vent_line(2, 2, 2, 1),
            create_vent_line(7, 0, 7, 4),
            create_vent_line(0, 9, 2, 9),
            create_vent_line(3, 4, 1, 4)
        ]
        self.assertEqual(result, expected_result)


    def test_countOverlaps(self):
        input_lines = [
            create_vent_line(0, 9, 5, 9),
            create_vent_line(9, 4, 3, 4),
            create_vent_line(2, 2, 2, 1),
            create_vent_line(7, 0, 7, 4),
            create_vent_line(0, 9, 2, 9),
            create_vent_line(3, 4, 1, 4)
        ]

        vents_map = vents.map_vent_lines(input_lines)
        result = vents.count_overlaps(vents_map)
        self.assertEqual(result, 5)


    def test_one_star_solution(self):
        result = vents.count_overlaps_for_straight_vents()
        self.assertEqual(result, 5294)


if __name__ == '__main__':
    unittest.main()
