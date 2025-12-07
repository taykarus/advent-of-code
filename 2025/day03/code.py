from aoc.utils import *

CURRENT_FILE = FILE


def part_1():
    lines = file_read_splitlines(CURRENT_FILE)
    total_joltage = 0
    for line_str in lines:
        line = [int(n) for n in line_str]
        max_index = line[:-1].index(max(line[:-1]))
        second_max_value = max(line[max_index+1:])
        joltage = int(str(line[max_index]) + str(second_max_value))
        total_joltage += joltage
    return total_joltage


def part_2():
    BATTERIES_COUNT = 12

    lines = file_read_splitlines(CURRENT_FILE)
    total_joltage = 0
    count = -1
    for line_str in lines:
        count += 1
        if count == 2:
            pass
        else:
            pass
        line = [int(n) for n in line_str]
        previous_max_index = -1
        max_numbers = []
        for i in range(BATTERIES_COUNT):
            limit_index = -BATTERIES_COUNT+i+1 if i != BATTERIES_COUNT-1 else len(line)
            search_list = line[previous_max_index+1:limit_index]
            max_index = line.index(max(search_list), previous_max_index+1)
            previous_max_index = max_index
            max_numbers.append(str(line[max_index]))
        joltage = int(''.join(max_numbers))
        total_joltage += int(joltage)
    return total_joltage


print('Part 1: ', part_1())
print('Part 2: ', part_2())
