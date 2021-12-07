import numpy as np


def part1(my_input):
    crab_locations = [int(n) for n in my_input[0].rstrip().split(",")]
    max_position = np.max(crab_locations)
    horizontal_position_costs = [0 for _ in range(max_position+1)]

    for crab in crab_locations:
        for i in range(1, max_position - crab + 1):
            horizontal_position_costs[crab + i] += i
        for i in range(1, crab + 1):
            horizontal_position_costs[crab - i] += i

    return np.min(horizontal_position_costs)


def get_fuel_costs(n):
    fuel_costs = [0]
    for i in range(1, n):
        fuel_costs.append(fuel_costs[i-1] + i)
    return fuel_costs


def part2(my_input):
    crab_locations = [int(n) for n in my_input[0].rstrip().split(",")]
    max_position = np.max(crab_locations)
    horizontal_position_costs = [0 for _ in range(max_position + 1)]

    fuel_costs = get_fuel_costs(max_position + 1)
    for crab in crab_locations:
        for i in range(1, max_position - crab + 1):
            horizontal_position_costs[crab + i] += fuel_costs[i]
        for i in range(1, crab + 1):
            horizontal_position_costs[crab - i] += fuel_costs[i]

    return np.min(horizontal_position_costs)
