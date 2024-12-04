import re

from aoc.utils import *


def part_1():
    lines = file_read(FILE).splitlines()
    writes = ['XMAS', 'SAMX']
    total = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            horizontal, vertical, diagonal, anti_diagonal = None, None, None, None
            if j+3 < len(lines[i]):
                horizontal = f'{lines[i][j]}{lines[i][j+1]}{lines[i][j+2]}{lines[i][j+3]}'
            if i+3 < len(lines):
                vertical = f'{lines[i][j]}{lines[i+1][j]}{lines[i+2][j]}{lines[i+3][j]}'
            if i+3 < len(lines) and j+3 < len(lines[i]):
                diagonal = f'{lines[i][j]}{lines[i+1][j+1]}{lines[i+2][j+2]}{lines[i+3][j+3]}'
                anti_diagonal = f'{lines[i][j+3]}{lines[i+1][j+2]}{lines[i+2][j+1]}{lines[i+3][j]}'
            for word in [horizontal, vertical, diagonal, anti_diagonal]:
                if word in writes:
                    total += 1
    return total


def part_2():
    lines = file_read(FILE).splitlines()
    writes = ['MAS', 'SAM']
    total = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if i+2 < len(lines) and j+2 < len(lines[i]):
                middle = f'{lines[i+1][j+1]}'
                if middle.upper() != 'A':
                    continue
                diagonal = f'{lines[i][j]}{middle}{lines[i+2][j+2]}'
                anti_diagonal = f'{lines[i][j+2]}{middle}{lines[i+2][j]}'
                if diagonal in writes and anti_diagonal in writes:
                    total += 1
    return total


print('Part 1: ', part_1())
print('Part 2: ', part_2())
