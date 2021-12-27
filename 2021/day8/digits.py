class DigitsParser:
    """
    Class for parsing input for seven-segment display
    """

    digits: list[tuple] = []

    def __init__(self, input_lines: list[str]):
        for line in input_lines:
            input_digits = line.split('|')[0].strip().split(' ')
            output_digits = line.split('|')[1].strip().split(' ')
            self.digits.append((input_digits, output_digits))

    def count_unique_segment_digits(self) -> int:
        """
        Counts number of 1, 4, 7 and 8 digits in output part of given input
        :return: Number of digits
        """
        counter = 0

        for digit in self.digits:
            for output_digit in digit[1]:
                if self.has_unique_number_of_segments(output_digit):
                    counter += 1

        return counter

    def has_unique_number_of_segments(self, digit: str):
        """
        1, 4, 7 and 8 are digits that have unique number of segments on when it's being displayed
        :param digit: string input containing segments that are on
        :return: information if digit is unique in matter of number of segments
        """
        match (len(digit)):
            case 2 | 3 | 4 | 7:
                return True
            case _:
                return False


