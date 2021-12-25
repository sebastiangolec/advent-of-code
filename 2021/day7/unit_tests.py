import unittest
from crabs import Crabs

class UnitTests(unittest.TestCase):
    initial_state = "16,1,2,0,4,2,7,1,2,14"
    params_list = [
        (1, 41),
        (2, 37),
        (3, 39),
        (10, 71)
    ]


    def test_calculating_cost(self):
        for position, expected_result in self.params_list:
            with self.subTest():
                crabs = Crabs(self.initial_state)
                result = crabs.calculate_cost(position)
                self.assertEqual(expected_result, result)


    def test_best_position(self):
        crabs = Crabs(self.initial_state)
        expected_result = (2, 37)
        result = crabs.find_best_position()

        self.assertEqual(expected_result[0], result[0])
        self.assertEqual(expected_result[1], result[1])


if __name__ == '__main__':
    unittest.main()