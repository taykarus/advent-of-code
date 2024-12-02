from aoc.utils import *


def get_int_lists_from_file():
    lines = file_read_lines(FILE)
    return [[int(l) for l in line.split()] for line in lines]


def is_between(value, start, end):
    return start <= value <= end


def is_all_increasing_or_decreasing(diff1, diff2):
    return (diff1 < 0 and diff2 < 0) or (diff1 > 0 and diff2 > 0)


def is_level_differ_valid(diff1, diff2, start, end):
    return is_between(abs(diff1), start, end) and is_between(abs(diff2), start, end)


def is_secure_list(l, check_sublist=False, index=0, original_list=None):
    if original_list is None:
        original_list = l

    if index > len(original_list):
        return False

    valid = True
    for i in range(2, len(l)):
        diff1 = l[i - 1] - l[i]
        diff2 = l[i - 2] - l[i - 1]
        if (not is_all_increasing_or_decreasing(diff1, diff2) or
                not is_level_differ_valid(diff1, diff2, 1, 3)):
            valid = False
            break
    if check_sublist:
        sublist = original_list[:index] + original_list[index+1:]
        return valid or is_secure_list(sublist, True, index+1, original_list)
    else:
        return valid


def part_1():
    lists = get_int_lists_from_file()

    total = 0
    for l in lists:
        if is_secure_list(l):
            total += 1
    return total


def part_2():
    lists = get_int_lists_from_file()

    total = 0
    for l in lists:
        if is_secure_list(l, check_sublist=True):
            total += 1
    return total


print('Part 1: ', part_1())
print('Part 2: ', part_2())
