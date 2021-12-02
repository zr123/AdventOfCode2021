import numpy as np


def part1(myinput):
    myinput = np.array(myinput, dtype=np.int64)
    return np.sum(myinput[1:] - myinput[:-1] > 0)


def get_windows(myinput):
    windows = []
    for i in range(2, len(myinput)):
        windows.append(np.sum(myinput[i - 2:i + 1]))
    return np.array(windows)


def part2(myinput):
    myinput = np.array(myinput, dtype=np.int64)
    windows = get_windows(myinput)
    return part1(windows)
