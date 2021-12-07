import numpy as np


def part1(myinput):
    crab_locations = [int(n) for n in myinput[0].rstrip().split(",")]
    max_position = np.max(crab_locations)
    horizontal_position_costs = [0 for _ in range(max_position+1)]

    for crab in crab_locations:
        for i in range(1, max_position - crab + 1):
            horizontal_position_costs[crab + i] += i
        for i in range(1, crab + 1):
            horizontal_position_costs[crab - i] += i

    return np.min(horizontal_position_costs)


def get_fuelcosts(n):
    fuelcosts = [0]
    for i in range(1, n):
        fuelcosts.append(fuelcosts[i-1] + i)
    return fuelcosts


def part2(myinput):
    crab_locations = [int(n) for n in myinput[0].rstrip().split(",")]
    max_position = np.max(crab_locations)
    weasel = [0 for _ in range(max_position + 1)]

    fuelcosts = get_fuelcosts(max_position + 1)
    for crab in crab_locations:
        for i in range(1, max_position - crab + 1):
            weasel[crab + i] += fuelcosts[i]
        for i in range(1, crab + 1):
            weasel[crab - i] += fuelcosts[i]

    return np.min(weasel)
