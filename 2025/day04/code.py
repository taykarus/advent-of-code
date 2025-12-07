from copy import deepcopy
from aoc.utils import *

CURRENT_FILE = FILE
MAX_ADJACENT_ROLLS = 4

def print_grid(lines):
    for line in lines:
        print(line)

def part_1():
    lines = file_read_splitlines(CURRENT_FILE)
    marked_rolls_lines = deepcopy(lines)
    accessible_rolls = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '.':
                continue

            adjacent_paper_rolls = 0

            # Previous Line
            if i > 0:
                if (j > 0) and lines[i-1][j-1] == '@':
                    adjacent_paper_rolls += 1
                if lines[i - 1][j] == '@':
                    adjacent_paper_rolls += 1
                if (j < len(lines[i])-1) and lines[i - 1][j+1] == '@':
                    adjacent_paper_rolls += 1

            # Same Line
            if (j > 0) and lines[i][j-1] == '@':
                adjacent_paper_rolls += 1
            if (j < len(lines[i])-1) and lines[i][j+1] == '@':
                adjacent_paper_rolls += 1

            # Next Line
            if i < len(lines)-1:
                if (j > 0) and lines[i+1][j-1] == '@':
                    adjacent_paper_rolls += 1
                if lines[i+1][j] == '@':
                    adjacent_paper_rolls += 1
                if (j < len(lines[i])-1) and lines[i+1][j+1] == '@':
                    adjacent_paper_rolls += 1

            if adjacent_paper_rolls < MAX_ADJACENT_ROLLS:
                temp_list = list(marked_rolls_lines[i])
                temp_list[j] = 'x'
                marked_rolls_lines[i] = ''.join(temp_list)
                accessible_rolls += 1

    print('Result:')
    for marked_rolls_line in marked_rolls_lines:
        print(marked_rolls_line)

    return accessible_rolls


def part_2():
    lines = file_read_splitlines(CURRENT_FILE)
    marked_rolls_lines = deepcopy(lines)

    print('Initial State:')
    print_grid(lines)

    total_removed_rolls = 0
    while True:
        itteration_removed_rolls = 0
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == '.':
                    continue

                adjacent_paper_rolls = 0

                # Previous Line
                if i > 0:
                    if (j > 0) and lines[i-1][j-1] == '@':
                        adjacent_paper_rolls += 1
                    if lines[i - 1][j] == '@':
                        adjacent_paper_rolls += 1
                    if (j < len(lines[i])-1) and lines[i - 1][j+1] == '@':
                        adjacent_paper_rolls += 1

                # Same Line
                if (j > 0) and lines[i][j-1] == '@':
                    adjacent_paper_rolls += 1
                if (j < len(lines[i])-1) and lines[i][j+1] == '@':
                    adjacent_paper_rolls += 1

                # Next Line
                if i < len(lines)-1:
                    if (j > 0) and lines[i+1][j-1] == '@':
                        adjacent_paper_rolls += 1
                    if lines[i+1][j] == '@':
                        adjacent_paper_rolls += 1
                    if (j < len(lines[i])-1) and lines[i+1][j+1] == '@':
                        adjacent_paper_rolls += 1

                if adjacent_paper_rolls < MAX_ADJACENT_ROLLS:
                    temp_list = list(marked_rolls_lines[i])
                    temp_list[j] = 'x'
                    marked_rolls_lines[i] = ''.join(temp_list)
                    itteration_removed_rolls += 1
                    total_removed_rolls += 1

        if itteration_removed_rolls == 0:
            break

        print(f'\nRemove {itteration_removed_rolls} rolls of paper:')
        print_grid(marked_rolls_lines)

        for i in range(len(marked_rolls_lines)):
            marked_rolls_lines[i] = marked_rolls_lines[i].replace('x', '.')

        lines = deepcopy(marked_rolls_lines)

    return total_removed_rolls


print('Part 1: ', part_1())
print('Part 2: ', part_2())