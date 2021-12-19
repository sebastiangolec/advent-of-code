import unittest
import vents


class Test(unittest.TestCase):
    def test_parseInput(self):
        with open('test_input', 'r') as file:
            input_lines = file.readlines()
            result = vents.parse(input_lines)
            expected_result = [
                vents.VentLine((0, 9), (5, 9)),
                vents.VentLine((8, 0), (0, 8)),
                vents.VentLine((9, 4), (3, 4)),
                vents.VentLine((2, 2), (2, 1)),
                vents.VentLine((7, 0), (7, 4)),
                vents.VentLine((6, 4), (2, 0)),
                vents.VentLine((0, 9), (2, 9)),
                vents.VentLine((3, 4), (1, 4)),
                vents.VentLine((0, 0), (8, 8)),
                vents.VentLine((5, 5), (8, 2))
            ]
            self.assertEqual(result, expected_result)
            file.close()


    def test_filterOutDiagonalLines(self):
        lines = [
            vents.VentLine((0, 9), (5, 9)),
            vents.VentLine((8, 0), (0, 8)),
            vents.VentLine((9, 4), (3, 4)),
            vents.VentLine((2, 2), (2, 1)),
            vents.VentLine((7, 0), (7, 4)),
            vents.VentLine((6, 4), (2, 0)),
            vents.VentLine((0, 9), (2, 9)),
            vents.VentLine((3, 4), (1, 4)),
            vents.VentLine((0, 0), (8, 8)),
            vents.VentLine((5, 5), (8, 2))
        ]

        result = vents.filter_out_diagonal_lines(lines)

        expected_result = [
            vents.VentLine((0, 9), (5, 9)),
            vents.VentLine((9, 4), (3, 4)),
            vents.VentLine((2, 2), (2, 1)),
            vents.VentLine((7, 0), (7, 4)),
            vents.VentLine((0, 9), (2, 9)),
            vents.VentLine((3, 4), (1, 4))
        ]
        self.assertEqual(result, expected_result)


    def test_countOverlaps(self):
        input_lines = [
            vents.VentLine((0, 9), (5, 9)),
            vents.VentLine((9, 4), (3, 4)),
            vents.VentLine((2, 2), (2, 1)),
            vents.VentLine((7, 0), (7, 4)),
            vents.VentLine((0, 9), (2, 9)),
            vents.VentLine((3, 4), (1, 4))
        ]

        result = vents.count_overlaps(input_lines)
        self.assertEqual(result, 5)


    def test_one_star_solution(self):
        result = vents.count_overlaps_for_straight_vents()
        self.assertEqual(result, 5294)


if __name__ == '__main__':
    unittest.main()
