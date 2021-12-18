import unittest
import main

class Test(unittest.TestCase):
    def test_parseInput(self):
        input = open('2021/day5/test_input', 'r').readlines()
        result = main.parse(input)
        expectedResult = [
            main.VentLine((0,9),(5,9)),
            main.VentLine((8,0),(0,8)),
            main.VentLine((9,4),(3,4)),
            main.VentLine((2,2),(2,1)),
            main.VentLine((7,0),(7,4)),
            main.VentLine((6,4),(2,0)),
            main.VentLine((0,9),(2,9)),
            main.VentLine((3,4),(1,4)),
            main.VentLine((0,0),(8,8)),
            main.VentLine((5,5),(8,2))
        ]
        self.assertEquals(result, expectedResult)

    def test_filterOutDiagonalLines(self):
        lines = [
            main.VentLine((0,9),(5,9)),
            main.VentLine((8,0),(0,8)),
            main.VentLine((9,4),(3,4)),
            main.VentLine((2,2),(2,1)),
            main.VentLine((7,0),(7,4)),
            main.VentLine((6,4),(2,0)),
            main.VentLine((0,9),(2,9)),
            main.VentLine((3,4),(1,4)),
            main.VentLine((0,0),(8,8)),
            main.VentLine((5,5),(8,2))
        ]

        result = main.filterOutDiagonalLines(lines)

        expectedResult = [
            main.VentLine((0,9),(5,9)),
            main.VentLine((9,4),(3,4)),
            main.VentLine((2,2),(2,1)),
            main.VentLine((7,0),(7,4)),
            main.VentLine((0,9),(2,9)),
            main.VentLine((3,4),(1,4))
        ]
        self.assertEquals(result, expectedResult)
    
    def test_countOverlaps(self):
        input = [
            main.VentLine((0,9),(5,9)),
            main.VentLine((9,4),(3,4)),
            main.VentLine((2,2),(2,1)),
            main.VentLine((7,0),(7,4)),
            main.VentLine((0,9),(2,9)),
            main.VentLine((3,4),(1,4))
        ]

        result = main.countOverlaps(input)
        self.assertEquals(result, 5)

if __name__ == '__main__':
    unittest.main()