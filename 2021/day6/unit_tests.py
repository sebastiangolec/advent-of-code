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
                ecosystem = LanternFish(self.initial_state)
                ecosystem.simulate(days)
                result = ecosystem.calculate_population()
                self.assertEqual(len(expected_result), result)


    def test_after_1_day(self):
        ecosystem = LanternFish(self.initial_state)
        ecosystem.simulate(1)
        result = ecosystem.calculate_population()
        expected_result = [2,3,2,0,1]
        self.assertEqual(len(expected_result), result)


    def test_after_2_days(self):
        ecosystem = LanternFish(self.initial_state)
        ecosystem.simulate(2)
        result = ecosystem.calculate_population()
        expected_result = [1,2,1,6,0,8]
        self.assertEqual(len(expected_result), result)


    def test_after_18_days(self):
        ecosystem = LanternFish(self.initial_state)
        ecosystem.simulate(18)
        result = ecosystem.calculate_population()
        self.assertEqual(26, result)


    def test_after_80_days(self):
        ecosystem = LanternFish(self.initial_state)
        ecosystem.simulate(80)
        result = ecosystem.calculate_population()
        self.assertEqual(5934, result)
    

    def test_after_256_days(self):
        ecosystem = LanternFish(self.initial_state)
        ecosystem.simulate(256)
        result = ecosystem.calculate_population()
        self.assertEqual(26984457539, result)


if __name__ == '__main__':
    unittest.main()