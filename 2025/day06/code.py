import re

from aoc.utils import *

CURRENT_FILE = FILE


def part_1():
    lines = file_read_splitlines(CURRENT_FILE)
    math_pattern = r'\d+|\+|\*'
    lines = [re.findall(math_pattern, l) for l in lines]

    total_lines = len(lines)
    total_columns = len(lines[0])

    grand_total = 0
    for i in range(total_columns):
        operation = lines[-1][i]
        column_total = None
        for j in range(total_lines-1):
            value = int(lines[j][i])
            if column_total is None:
                column_total = value
            else:
                if operation == '+':
                    column_total += value
                elif operation == '*':
                    column_total *= value
        grand_total += column_total

    return grand_total


def part_2():
    lines = file_read_splitlines(CURRENT_FILE)

    total_lines = len(lines)
    total_columns = len(lines[0])

    grand_total = 0

    operation = None
    values = []
    actual_operand = ''
    for i in range(total_columns-1, -1, -1):
        is_column_empty = True

        for j in range(total_lines):
            value = lines[j][i]
            if value != ' ':
                is_column_empty = False

            if value == ' ':  # last line or end of number
                if j == total_lines-1:  # last line
                    if actual_operand:
                        values.append(int(actual_operand))
                    actual_operand = ''
                    break
                else:  # end of number
                    if actual_operand:
                        values.append(int(actual_operand))
                    actual_operand = ''
            elif value in ('+', '*'):  # last line with operation
                operation = value
                if actual_operand:
                    values.append(int(actual_operand))
                actual_operand = ''
                break

            actual_operand += value  # append operand digit

        if i == 0 or is_column_empty:  # first column reached or empty column splitting operation group
            column_total = values.pop(0)
            for value in values:
                if operation == '+':
                    column_total += value
                elif operation == '*':
                    column_total *= value
            grand_total += column_total

            operation = None
            values = []
            actual_operand = ''

    return grand_total


print('Part 1: ', part_1())
print('Part 2: ', part_2())
