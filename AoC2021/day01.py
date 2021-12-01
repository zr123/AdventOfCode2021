import numpy as np


def part1(myinput):
    return np.sum(myinput[1:] - myinput[:-1] > 0)


def get_windows(myinput):
    windows = []
    for i in range(2, len(myinput)):
        windows.append(np.sum(myinput[i - 2:i + 1]))
    return np.array(windows)


def part2(myinput):
    windows = get_windows(myinput)
    return part1(windows)
