from aoc.utils import *


def get_sorted_left_right_from_file():
    lines = file_read_lines(FILE)

    left, right = [], []
    for line in lines:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

    left.sort()
    right.sort()

    return left, right


def part_1():
    left, right = get_sorted_left_right_from_file()

    total = 0
    for l, r in zip(left, right):
        total += abs(l - r)

    return total


def part_2():
    left, right = get_sorted_left_right_from_file()

    total = 0
    for i in range(len(left)):
        left_times = 0
        for j in range(len(right)):
            if left[i] == right[j]:
                left_times += 1
        total += left_times * left[i]

    return total


print('Part 1: ', part_1())
print('Part 2: ', part_2())
