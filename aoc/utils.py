FILE = 'input.txt'
FILE_EXAMPLE = 'example.txt'


def file_read_lines(filename):
    with open(filename) as f:
        return f.readlines()


def split_int(line):
    return [int(level) for level in line.split()]
