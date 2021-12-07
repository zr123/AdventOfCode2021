import numpy as np


def simulate(initial_state, days):
    numbers = [int(n) for n in initial_state.split(",")]
    # fish[internal_timer] = count
    fish = [0 for _ in range(9)]
    for n in numbers:
        fish[n] += 1

    for day in range(days):
        created_lantern_fish = fish[0]
        fish[:8] = fish[1:9]
        fish[8] = created_lantern_fish
        fish[6] += created_lantern_fish

    return np.sum(fish)


def part1(my_input):
    return simulate(my_input[0], 80)


def part2(my_input):
    return simulate(my_input[0], 256)
