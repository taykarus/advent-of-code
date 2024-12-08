from aoc.utils import *

GUARD_POSITIONS = ['^', 'v', '<', '>']


def replace_str_index(string, value, index):
    l = list(string)
    l[index] = value
    return ''.join(l)


def get_start_stop_step_by_direction(direction, i, guard_index, line_size, lines_length):
    direction_parameters = {
        '^': {
            'start': i,
            'stop': -1,
            'step': -1,
        },
        '>': {
            'start': guard_index,
            'stop': line_size,
            'step': 1,
        },
        'v': {
            'start': i,
            'stop': lines_length,
            'step': 1,
        },
        '<': {
            'start': guard_index,
            'stop': -1,
            'step': -1,
        }
    }

    if direction not in direction_parameters:
        raise ValueError('Invalid direction')

    start, stop, step = direction_parameters[direction].values()
    start, stop, step = int(start), int(stop), int(step)

    return start, stop, step


def get_next_direction(direction):
    if direction == '<':
        return '^'
    elif direction == '^':
        return '>'
    elif direction == '>':
        return 'v'
    elif direction == 'v':
        return '<'


def update_str_index(string, index, value):
    l = list(string)
    l[index] = value
    return ''.join(l)


def part_1():
    file = file_read(FILE)
    lines = file.splitlines()
    direction_changed = True
    previous_direction_changed = False
    while direction_changed:
        direction_changed = False
        for i, line in enumerate(lines):
            guard_index = next((line.index(position) for position in GUARD_POSITIONS if position in line), None)
            if not guard_index:
                continue

            direction = line[guard_index]
            start, stop, step = get_start_stop_step_by_direction(direction, i, guard_index, len(lines), len(lines))
            for j in range(start, stop, step):
                next_direction = get_next_direction(direction)
                if direction in ('^', 'v'):
                    l = list(lines[j])
                    if l[guard_index] != '#':
                        lines[j] = update_str_index(lines[j], guard_index, 'X')
                        previous_direction_changed = False
                    elif l[guard_index] == '#' or j == stop - step:
                        line_index = j
                        if l[guard_index] == '#':
                            line_index -= step
                        if previous_direction_changed:
                            break
                        lines[line_index] = update_str_index(lines[line_index], guard_index, next_direction)
                        direction_changed = True
                        previous_direction_changed = True
                        break
                elif direction in ('<', '>'):
                    l = list(lines[i])
                    column_index = j
                    if l[j] != '#':
                        lines[i] = update_str_index(lines[i], j, 'X')
                        previous_direction_changed = False
                    elif j == stop - step or l[j] == '#':
                        if l[j] == '#':
                            column_index -= step
                        if previous_direction_changed:
                            break
                        lines[i] = update_str_index(lines[i], column_index, next_direction)
                        direction_changed = True
                        previous_direction_changed = True
                        break
    return sum(line.count('X') for line in lines)


def part_2():
    file = file_read(FILE)
    lines = file.splitlines()
    guard_positions = ['^', 'v', '<', '>']
    original_lines = list(lines)
    total = 0
    for x in range(len(lines)):
        print(x)
        for y in range(len(lines[x])):
            is_valid = False
            lines = list(original_lines)
            x_y_positions = {}
            tmp_list = list(lines[x])
            if tmp_list == '#':
                continue
            tmp_list[y] = '#'
            lines[x] = ''.join(tmp_list)
            direction_changed = True
            while direction_changed:
                if is_valid:
                    break
                direction_changed = False
                for i, line in enumerate(lines):
                    if is_valid:
                        break
                    guard_index = next((line.index(position) for position in guard_positions if position in line), None)
                    if guard_index:
                        direction = line[guard_index]
                        start, stop, step = get_start_stop_step_by_direction(direction, i, guard_index, len(lines), len(lines))
                        for j in range(start, stop, step):
                            next_direction = get_next_direction(direction)
                            if direction in ('^', 'v'):
                                l = list(lines[j])
                                if l[guard_index] != '#':
                                    l[guard_index] = 'X'
                                    key = f'{j},{guard_index}'
                                    if direction in x_y_positions.get(key, []):
                                        is_valid = True
                                        total += 1
                                        break
                                    x_y_positions[key] = x_y_positions.get(key, []) + [direction]
                                    lines[j] = ''.join(l)
                                elif j == stop - step or l[guard_index] == '#':
                                    line_index = j
                                    if l[guard_index] == '#':
                                        line_index -= step
                                    lines[line_index] = update_str_index(lines[line_index], guard_index, next_direction)
                                    direction_changed = True
                                    break
                            elif direction in ('<', '>'):
                                l = list(lines[i])
                                if l[j] != '#':
                                    l[j] = 'X'
                                    key = f'{i},{j}'
                                    if direction in x_y_positions.get(key, []):
                                        is_valid = True
                                        total += 1
                                        break
                                    x_y_positions[key] = x_y_positions.get(key, []) + [direction]
                                    lines[i] = update_str_index(l, j, 'X')
                                elif j == stop - step or l[j] == '#':
                                    column_index = j
                                    if l[j] == '#':
                                        column_index -= step
                                    lines[i] = update_str_index(lines[i], column_index, next_direction)
                                    direction_changed = True
                                    break
                        if is_valid:
                            break
                if is_valid:
                    break
    return total


print('Part 1: ', part_1())
print('Part 2: ', part_2())