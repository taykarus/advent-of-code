FILE = 'input.txt'
FILE_EXAMPLE = 'example.txt'


def file_read_lines(filename):
    with open(filename) as f:
        return f.readlines()


frl = _frl = file_read_lines
