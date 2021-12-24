import unittest
from lantern_fish import LanternFish

class UnitTests(unittest.TestCase):
    initial_state = "3,4,3,1,2"
    params_list = [
        ( 1, [2,3,2,0,1]),
        ( 2, [1,2,1,6,0,8]),
        ( 3, [0,1,0,5,6,7,8]),
        ( 4, [6,0,6,4,5,6,7,8,8]),
        ( 5, [5,6,5,3,4,5,6,7,7,8]),
        ( 6, [4,5,4,2,3,4,5,6,6,7]),
        ( 7, [3,4,3,1,2,3,4,5,5,6]),
        ( 8, [2,3,2,0,1,2,3,4,4,5]),
        ( 9, [1,2,1,6,0,1,2,3,3,4,8]),
        (10, [0,1,0,5,6,0,1,2,2,3,7,8]),
        (11, [6,0,6,4,5,6,0,1,1,2,6,7,8,8,8]),
        (12, [5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8]),
        (13, [4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8]),
        (14, [3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8]),
        (15, [2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7]),
        (16, [1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8]),
        (17, [0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8]),
        (18, [6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8])
    ]


    def test_sumulation(self):
        for days, expected_result in self.params_list:
            with self.subTest():
                result = LanternFish(self.initial_state).simulate(days)
                self.assertEqual(expected_result, result)


    def test_after_1_day(self):
        result = LanternFish(self.initial_state).simulate(1)
        expected_result = [2,3,2,0,1]
        self.assertEqual(expected_result, result)


    def test_after_2_days(self):
        result = LanternFish(self.initial_state).simulate(2)
        expected_result = [1,2,1,6,0,8]
        self.assertEqual(expected_result, result)


    def test_after_18_days(self):
        result = LanternFish(self.initial_state).simulate(18)
        expected_result = [6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8]
        self.assertEqual(expected_result, result)
        self.assertEqual(26, len(result))


    def test_after_80_days(self):
        result = LanternFish(self.initial_state).simulate(80)
        self.assertEqual(5934, len(result))        


if __name__ == '__main__':
    unittest.main()