import unittest
from digits import DigitsParser


class UnitTest(unittest.TestCase):
    def test_digits_with_unique_number_of_segments(self):
        with open('test_input', 'r') as file:
            digits_parser = DigitsParser(file.readlines())
            self.assertEqual(26, digits_parser.count_unique_segment_digits())


if __name__ == '__main__':
    unittest.main()