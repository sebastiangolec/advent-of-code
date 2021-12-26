from digits import DigitsParser

with open('input', 'r') as file:
    digits_parser = DigitsParser(file.readlines())
    print(digits_parser.count_unique_segment_digits())