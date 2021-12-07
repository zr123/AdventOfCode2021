import numpy as np


def part1(my_input):
    my_input = np.array(my_input, dtype=np.int64)
    return np.sum(my_input[1:] - my_input[:-1] > 0)


def get_windows(my_input):
    windows = []
    for i in range(2, len(my_input)):
        windows.append(np.sum(my_input[i - 2:i + 1]))
    return np.array(windows)


def part2(my_input):
    my_input = np.array(my_input, dtype=np.int64)
    windows = get_windows(my_input)
    return part1(windows)
