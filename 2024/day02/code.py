from aoc.utils import *

REPORT_VALID_START = 1
REPORT_VALID_END = 3


def split_int_from_file():
    lines = file_read_lines(FILE)
    return [split_int(line) for line in lines]


def calculate_pair_diff_by_index(levels, i):
    return levels[i] - levels[i-1]


def is_diff_valid(diff):
    if diff == 0:
        return False
    return REPORT_VALID_START <= abs(diff) <= REPORT_VALID_END


def is_secure_list(levels, check_sublist=False, index=0, original_list=None):
    if original_list is None:
        original_list = levels

    if index > len(original_list):
        return False

    valid = True
    is_list_increasing = None
    for i in range(1, len(levels)):
        diff = calculate_pair_diff_by_index(levels, i)

        is_pair_increasing = diff > 0
        if is_list_increasing is None:
            is_list_increasing = is_pair_increasing

        if not is_diff_valid(diff) or is_pair_increasing != is_list_increasing:
            valid = False
            break

    if valid:
        return True
    elif check_sublist:
        sublist = original_list[:index] + original_list[index + 1:]
        return is_secure_list(sublist, True, index + 1, original_list)

    return False


def part_1():
    lines = split_int_from_file()
    return sum([is_secure_list(line) for line in lines])


def part_2():
    lines = split_int_from_file()
    return sum([is_secure_list(line, check_sublist=True) for line in lines])


print('Part 1: ', part_1())
print('Part 2: ', part_2())
