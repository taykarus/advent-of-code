from copy import deepcopy
from aoc.utils import *

CURRENT_FILE = FILE


def part_1():
    lines = file_read_splitlines(CURRENT_FILE)
    blank_line_index = lines.index('')
    fresh_ranges, ingredients = lines[:blank_line_index], lines[blank_line_index+1:]

    fresh_ranges_tuples = []
    for fresh_range in fresh_ranges:
        start, end = fresh_range.split('-')
        fresh_ranges_tuples.append((int(start), int(end)))

    ingredients = [int(i) for i in ingredients]
    total_fresh_ingredients = 0
    for ingredient in ingredients:
        for fresh_range in fresh_ranges_tuples:
            if fresh_range[0] <= ingredient <= fresh_range[1]:
                total_fresh_ingredients += 1
                break

    return total_fresh_ingredients


def part_2():
    lines = file_read_splitlines(CURRENT_FILE)
    blank_line_index = lines.index('')
    fresh_ranges = lines[:blank_line_index]

    fresh_ranges_lists = []
    for fresh_range in fresh_ranges:
        start, end = fresh_range.split('-')
        fresh_ranges_lists.append([int(start), int(end)])

    fresh_ranges_lists.sort(key=lambda item: item[0])

    merged_fresh_ranges = [list(fresh_ranges_lists.pop(0))]
    for i in range(len(fresh_ranges_lists)):
        for j in range(len(merged_fresh_ranges)):
            if merged_fresh_ranges[j][0] <= fresh_ranges_lists[i][0] <= merged_fresh_ranges[j][1]: # merged_fresh_range start contains fresh_rage start
                if merged_fresh_ranges[j][1] >= fresh_ranges_lists[i][1]:
                    break # it's already contained
                else:
                    merged_fresh_ranges[j][1] = fresh_ranges_lists[i][1]
                    break # update merged_fresh_range ending
        else:
            merged_fresh_ranges.append(list(fresh_ranges_lists[i])) # no range found to merge, add it

    total_fresh_ingredients = 0
    for merged_fresh_range in merged_fresh_ranges:
        start, end = merged_fresh_range
        total_fresh_ingredients += end - start + 1
    return total_fresh_ingredients


print('Part 1: ', part_1())
print('Part 2: ', part_2())