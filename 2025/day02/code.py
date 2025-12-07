from aoc.utils import *

CURRENT_FILE = FILE


def part_1():
    file = file_read(CURRENT_FILE)

    invalid_numbers_sum = 0

    number_ranges = file.split(',')
    for number_range in number_ranges:
        start, end = [int(n) for n in number_range.split('-')]
        for number in range(start, end + 1):
            number_length = int(len(str(number)))
            if is_odd(number_length):
                continue

            half_length = int(number_length/2)
            first_half = str(number)[:half_length]
            last_half = str(number)[half_length:]
            if first_half == last_half:
                invalid_numbers_sum += number

    return invalid_numbers_sum


def part_2():
    file = file_read(CURRENT_FILE)

    invalid_numbers = set()

    number_ranges = file.split(',')
    for number_range in number_ranges:
        start, end = [int(n) for n in number_range.split('-')]
        for number in range(start, end + 1):
            for i in range(1, len(str(number))):
                if len(str(number)) % i != 0:
                    continue

                full_length_number =  int(str(number)[:i] * (len(str(number)) // i))
                if start <= full_length_number <= end:
                    invalid_numbers.add(full_length_number)

    invalid_numbers_sum = sum(invalid_numbers)
    return invalid_numbers_sum


print('Part 1: {} - Time: {}'.format(*measure_time(part_1)))
print('Part 2: {} - Time: {}'.format(*measure_time(part_2)))
