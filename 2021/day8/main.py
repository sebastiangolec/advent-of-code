from digits import DigitsParser

with open('input', 'r') as file:
    print('========== Parsing input ==========')
    digits_parser = DigitsParser(file.readlines())
    print(digits_parser.count_output_digits_with_unique_number_of_segments())
    digits_parser.decode()
    for cipher in digits_parser.ciphers:
        print(cipher.print())
    file.close()

with open('test_input', 'r') as file:
    print('\n\n\n========== Parsing test input ==========')
    digits_parser = DigitsParser(file.readlines())
    digits_parser.decode()
    for cipher in digits_parser.ciphers:
        print(cipher.print())
    file.close()
