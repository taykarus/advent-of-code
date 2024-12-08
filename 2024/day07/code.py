from aoc.utils import *


def part_1():
    lines = file_read(FILE).splitlines()
    calibration_total = 0
    for line in lines:
        result_test, numbers = line.split(': ')
        result_test = int(result_test)
        numbers = split_int(numbers, ' ')
        for i in range(2 ** (len(numbers) - 1)):
            binary = list(str(bin(i)[2:]).zfill(len(numbers) - 1))
            total = numbers[0]
            for j in range(1, len(numbers)):
                if binary[j - 1] == '1':
                    total *= numbers[j]
                else:
                    total += numbers[j]
            if total == result_test:
                calibration_total += total
                break
    return calibration_total


def ternary(n):
    if n == 0:
        return '0'
    numbers = []
    while n:
        n, r = divmod(n, 3)
        numbers.append(str(r))
    return ''.join(reversed(numbers))


def part_2():
    lines = file_read(FILE).splitlines()
    calibration_total = 0
    for line in lines:
        result_test, numbers = line.split(': ')
        result_test = int(result_test)
        numbers = split_int(numbers, ' ')
        for i in range(3 ** (len(numbers) - 1)):
            t = list(str(ternary(i)).zfill(len(numbers) - 1))
            total = numbers[0]
            for j in range(1, len(numbers)):
                if t[j - 1] == '0':
                    total *= numbers[j]
                elif t[j - 1] == '1':
                    total += numbers[j]
                else:
                    total = int(f'{total}{numbers[j]}')
            if total == result_test:
                calibration_total += total
                break
    return calibration_total


print('Part 1: ', part_1())
print('Part 2: ', part_2())
