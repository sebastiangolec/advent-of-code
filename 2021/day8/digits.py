class DigitsParser:
    digits: list[tuple] = []

    def __init__(self, input_lines: list[str]):
        for line in input_lines:
            input_digits = line.split('|')[0].strip().split(' ')
            output_digits = line.split('|')[1].strip().split(' ')
            self.digits.append((input_digits, output_digits))

    def count_unique_segment_digits(self) -> int:
        counter = 0

        for digit in self.digits:
            for output_digit in digit[1]:
                if self.has_unique_number_of_segments(output_digit):
                    counter += 1

        return counter

    def has_unique_number_of_segments(self, digit: str):
        match (len(digit)):
            case 2 | 3 | 4 | 7:
                return True
            case _:
                return False


