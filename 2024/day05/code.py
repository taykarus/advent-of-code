from aoc.utils import *


def get_sort_rules_and_updates_from_file():
    lines = file_read(FILE).splitlines()
    sort_rules, updates = [], []
    is_sort_rule = True
    for line in lines:
        if line == '':
            is_sort_rule = False
            continue
        if is_sort_rule:
            sort_rules.append(split_int(line, '|'))
        else:
            updates.append(split_int(line, ','))
    return sort_rules, updates


def is_right_update(sort_rules, update):
    right_update = True
    for x, y in sort_rules:
        try:
            x_index = update.index(x)
            y_index = update.index(y)
        except ValueError:
            continue
        if x_index > y_index:
            right_update = False
            break
    return right_update


def part_1():
    sort_rules, updates = get_sort_rules_and_updates_from_file()
    total = 0
    for update in updates:
        if is_right_update(sort_rules, update):
            middle_index = len(update)//2
            total += update[middle_index]
    return total


def part_2():
    sort_rules, updates = get_sort_rules_and_updates_from_file()

    total = 0
    for update in updates:
        right_update = is_right_update(sort_rules, update)
        if not right_update:
            sorted_update = []
            for i in range(len(update)):
                for j in range(len(update)):
                    temp_update = list(sorted_update)
                    temp_update.insert(j, update[i])
                    if is_right_update(sort_rules, temp_update):
                        sorted_update = temp_update
                        break
                    else:
                        continue
            middle_index = len(sorted_update) // 2
            total += sorted_update[middle_index]
    return total


print('Part 1: ', part_1())
print('Part 2: ', part_2())
