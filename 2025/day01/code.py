from aoc.utils import *

CURRENT_FILE = FILE
INITIAL_DIAL_START = 50


def part_1(verbose=False):
    lines = file_read_splitlines(CURRENT_FILE)

    dial = INITIAL_DIAL_START
    password = 0

    for line in lines:
        direction, distance = line[0], int(line[1:])
        if direction == 'L':
            dial -= distance
        elif direction == 'R':
            dial += distance

        dial = dial % 100
        if dial == 0:
            password += 1

        if verbose:
            print(f'Direction: {direction}\nDistance: {distance}\nDial: {dial}\nPassword: {password}\n')

    return password


def part_2(verbose=False):
    lines = file_read_splitlines(CURRENT_FILE)

    dial = INITIAL_DIAL_START
    password = 0

    for line in lines:
        start_dial = dial
        direction, distance = line[0], int(line[1:])

        if direction == 'L':
            dial -= distance
            password += abs(dial) // 100
            if dial <= 0 and start_dial != 0:
                password += 1
        elif direction == 'R':
            dial += distance
            password += dial // 100

        dial = dial % 100

        if verbose:
            print(f'Direction: {direction}\nDistance: {distance}\nDial: {dial}\nPassword: {password}\n')

    return password


print('Part 1: ', part_1(verbose=False))
print('Part 2: ', part_2(verbose=False))
