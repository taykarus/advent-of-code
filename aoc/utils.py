FILE = 'input.txt'
FILE_EXAMPLE = 'example.txt'
FILE_EXAMPLE2 = 'example2.txt'


def file_read(filename):
    with open(filename) as f:
        return f.read()


def file_read_lines(filename):
    with open(filename) as f:
        return f.readlines()


def clean_list(dirty_list):
    return [element for element in dirty_list if element]


def split_int(line):
    return [int(level) for level in line.split()]
