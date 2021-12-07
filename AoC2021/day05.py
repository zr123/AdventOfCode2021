import numpy as np


def part1(my_input):
    field = np.zeros((1000, 1000))
    for line in my_input:
        x1, y1, x2, y2 = [int(n) for n in line.replace(" -> ", ",").rstrip().split(",")]
        if x1 == x2 or y1 == y2:
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            field[y1:y2+1, x1:x2+1] += 1

    return len(field[field > 1])


def part2(my_input):
    field = np.zeros((1000, 1000))
    for line in my_input:
        x1, y1, x2, y2 = [int(n) for n in line.replace(" -> ", ",").rstrip().split(",")]
        if x1 == x2 or y1 == y2:
            # horizontal / vertical
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            field[y1:y2 + 1, x1:x2 + 1] += 1
        else:
            # diagonal
            y_sign, x_sign = 1, 1
            if y1 > y2:
                y_sign = -1
            if x1 > x2:
                x_sign = -1
            for i in range(abs(x2-x1)+1):
                field[y1+i*y_sign, x1+i*x_sign] += 1

    return len(field[field > 1])
