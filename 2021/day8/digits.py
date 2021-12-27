class Digit:
    word: str
    digit: int
    possible_digits: list[int]
    is_decoded: bool = False
    has_unique_number_of_segments: bool = False  # True only for 1, 4, 7 and 8 digits

    def __init__(self, word: str):
        self.word = word
        self.possible_digits = []
        self.digit = None
        self.decode_by_length(len(word))

    def decode_by_length(self, word_length: int):
        match word_length:
            case 2:
                self.digit = 1
                self.possible_digits.append(1)
                self.is_decoded = True
                self.has_unique_number_of_segments = True
            case 3:
                self.digit = 7
                self.possible_digits.append(7)
                self.is_decoded = True
                self.has_unique_number_of_segments = True
            case 4:
                self.digit = 4
                self.possible_digits.append(4)
                self.is_decoded = True
                self.has_unique_number_of_segments = True
            case 5:
                self.possible_digits.append(2)
                self.possible_digits.append(3)
                self.possible_digits.append(5)
            case 6:
                self.possible_digits.append(0)
                self.possible_digits.append(6)
                self.possible_digits.append(9)
            case 7:
                self.digit = 8
                self.possible_digits.append(8)
                self.is_decoded = True
                self.has_unique_number_of_segments = True

    def decode_by_one(self, word: str):
        if not self.is_decoded:
            if word[0] in self.word and word[1] in self.word:
                self.remove_from_possible_digits([2, 5, 6])
            else:
                self.remove_from_possible_digits([0, 1, 3, 4, 7, 8, 9])

            self.check_if_decoded()

    def decode_by_seven(self, word: str):
        if not self.is_decoded:
            if word[0] in self.word and word[1] in self.word and word[2] in self.word:
                self.remove_from_possible_digits([2, 5, 6])
            else:
                self.remove_from_possible_digits([0, 1, 3, 4, 7, 8, 9])

            self.check_if_decoded()

    def decode_by_four(self, word: str):
        if not self.is_decoded:
            if word[0] in self.word and word[1] in self.word and word[2] in self.word and word[3] in self.word:
                self.remove_from_possible_digits([0, 2, 3, 5, 6])
            else:
                self.remove_from_possible_digits([4, 8, 9])

            self.check_if_decoded()

    def check_if_decoded(self):
        if not self.is_decoded and len(self.possible_digits) == 1:
            self.digit = self.possible_digits[0]
            self.is_decoded = True

    def remove_from_possible_digits(self, numbers: list[int]):
        for number in numbers:
            if number in self.possible_digits:
                self.possible_digits.remove(number)


class Cipher:
    input_digits: list[Digit]
    output_digits: list[Digit]

    def __init__(self, cipher_string: str):
        self.input_digits = []
        self.output_digits = []
        input_part = cipher_string.split('|')[0].strip().split(' ')
        output_part = cipher_string.split('|')[1].strip().split(' ')

        for word in input_part:
            self.input_digits.append(Digit(word))

        for word in output_part:
            self.output_digits.append(Digit(word))

    def decode_by_elimination(self):
        one_digit_word = self.find_word_by_number(1)
        four_digit_word = self.find_word_by_number(4)
        seven_digit_word = self.find_word_by_number(7)

        if one_digit_word[0] is True:
            for digit in self.input_digits + self.output_digits:
                digit.decode_by_one(one_digit_word[1])

        if four_digit_word[0] is True:
            for digit in self.input_digits + self.output_digits:
                digit.decode_by_four(four_digit_word[1])

        if seven_digit_word[0] is True:
            for digit in self.input_digits + self.output_digits:
                digit.decode_by_seven(seven_digit_word[1])

    def find_word_by_number(self, number: int) -> (bool, str):
        result = False, ''

        for digit in self.input_digits + self.output_digits:
            if digit.digit is not None and number == digit.digit:
                result = True, digit.word
                break

        return result

    def print(self):
        output_string = ''

        for digit in self.input_digits:
            if digit.is_decoded:
                output_string += str(digit.digit)
            else:
                output_string += digit.word
            output_string += ' '

        output_string += '| '

        for digit in self.output_digits:
            if digit.is_decoded:
                output_string += str(digit.digit)
            else:
                output_string += digit.word
            output_string += ' '

        return output_string


class DigitsParser:
    ciphers: list[Cipher]

    def __init__(self, input_lines: list[str]):
        self.ciphers = []
        for line in input_lines:
            self.ciphers.append(Cipher(line))

    def count_output_digits_with_unique_number_of_segments(self) -> int:
        """
        Counts number of digits in output part that have unique_number_of_segments
        1, 4, 7 and 8 has unique number of segments
        :return: counted number
        """
        counter = 0

        for cipher in self.ciphers:
            for output_digit in cipher.output_digits:
                if output_digit.has_unique_number_of_segments:
                    counter += 1

        return counter

    def decode(self):
        for cipher in self.ciphers:
            cipher.decode_by_elimination()
