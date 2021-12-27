import unittest
from digits import DigitsParser


class UnitTest(unittest.TestCase):
    def test_digits_with_unique_number_of_segments(self):
        with open('test_input', 'r') as file:
            digits_parser = DigitsParser(file.readlines())
            file.close()

            self.assertEqual(26, digits_parser.count_unique_segment_digits())

    # TODO reimplement according to changes in data structure of solution
    # def test_decoding_small_example(self):
    #     input_line = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']
    #     expected_input_digits = [8, 5, 2, 3, 7, 9, 6, 4, 0, 1]
    #     expected_output_digits = [5, 3, 5, 3]
    #     digits_parser = DigitsParser(input_line)
    #     result = digits_parser.decode()
    #
    #     self.assertEqual((expected_input_digits, expected_output_digits), result)
    #
    # def test_decoding_for_larger_sample(self):
    #     with open('test_input', 'r') as file:
    #         digits_parser = DigitsParser(file.readlines())
    #         file.close()
    #         expected_result = [8394, 9781, 1197, 9361, 4873, 8418, 4548, 1625, 8717, 4315]
    #         result = digits_parser.decode()
    #
    #         for expected_number, result_number in zip(expected_result, result):
    #             self.assertEqual(expected_number, result_number)


if __name__ == '__main__':
    unittest.main()