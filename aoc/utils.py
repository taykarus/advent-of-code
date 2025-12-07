FILE = 'input.txt'
FILE_EXAMPLE = 'example.txt'
FILE_EXAMPLE2 = 'example2.txt'
FILE_EXAMPLE3 = 'example3.txt'


def file_read(filename):
    with open(filename) as f:
        return f.read()


def file_read_lines(filename):
    with open(filename) as f:
        return f.readlines()


def file_read_splitlines(filename):
    with open(filename) as f:
        return f.read().splitlines()


def clean_list(dirty_list):
    return [element for element in dirty_list if element]


def split_int(line, separator=None):
    return [int(level) for level in line.split(separator)]


def measure_time(func, *args, **kwargs):
    from time import time
    start_time = time()
    result = func(*args, **kwargs)
    elapsed_time = time() - start_time
    return result, elapsed_time


def is_even(number):
    return number % 2 == 0


def is_odd(number):
    return number % 2 == 1
