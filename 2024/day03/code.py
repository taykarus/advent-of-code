import re

from aoc.utils import *


def split_operations_from_file1():
    file = file_read(FILE)
    pattern = r'mul\(([0-9]{1,3}),([0-9]{1,3})\)'
    return re.findall(pattern, file)


def part_1():
    operations = split_operations_from_file1()
    total = 0
    for operation in operations:
        total += int(operation[0]) * int(operation[1])
    return total


def split_operations_from_file2():
    file = file_read(FILE)
    pattern = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)|(don't\(\))|(do\(\))"
    matches = re.findall(pattern, file)
    cleaned_matches = [clean_list(match) for match in matches]
    return cleaned_matches


def part_2():
    operations = split_operations_from_file2()
    total = 0
    do = True
    for operation in operations:
        if len(operation) == 1:
            if operation[0] == "do()":
                do = True
            elif operation[0] == "don't()":
                do = False
        elif do:
            total += int(operation[0]) * int(operation[1])
    return total


print('Part 1: ', part_1())
print('Part 2: ', part_2())
