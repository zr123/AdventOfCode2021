import numpy as np


def simulate(initial_state, days):
    numbers = [int(n) for n in initial_state.split(",")]
    # fish[internal_timer] = count
    fish = [0 for i in range(9)]
    for n in numbers:
        fish[n] += 1

    for day in range(days):
        created_lanternfish = fish[0]
        fish[:8] = fish[1:9]
        fish[8] = created_lanternfish
        fish[6] += created_lanternfish

    return np.sum(fish)


def part1(myinput):
    return simulate(myinput[0], 80)


def part2(myinput):
    return simulate(myinput[0], 256)
