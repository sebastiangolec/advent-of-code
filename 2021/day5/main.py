"""--- Day 5: Hydrothermal Venture ---"""
import vents

def main():
    input_lines = open('input', 'r').readlines()
    vent_lines = vents.parse(input_lines)
    vent_lines = vents.filter_out_diagonal_lines(vent_lines)
    result = vents.count_overlaps(vent_lines)
    print(result)


main()
