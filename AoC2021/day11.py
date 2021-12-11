import numpy as np


def str_to_ints(string):
    return [int(char) for char in string]


def flash(octopus_map, y, x):
    y_min, y_max, x_min, x_max = y-1, y+2, x-1, x+2
    if y_min < 0:
        y_min = 0
    if x_min < 0:
        x_min = 0
    if y_max > 10:
        y_max = 10
    if x_max > 10:
        x_max = 10

    octopus_map[y_min:y_max, x_min:x_max] += 1
    # santa?! what does the scanner say about the energy level?!
    octopus_map[y, x] = -9001

    for y_i in range(y_min, y_max):
        for x_i in range(x_min, x_max):
            if octopus_map[y_i, x_i] > 9:
                flash(octopus_map, y_i, x_i)


def timestep(octopus_map):
    octopus_map += 1
    for y_i in range(octopus_map.shape[0]):
        for x_i in range(octopus_map.shape[1]):
            if octopus_map[y_i, x_i] > 9:
                flash(octopus_map, y_i, x_i)

    flash_count = len(octopus_map[octopus_map < 0])
    octopus_map[octopus_map < 0] = 0
    return flash_count


def part1(my_input):
    octopus_map = np.array([str_to_ints(s.rstrip()) for s in my_input])
    total_flashes = 0
    for i in range(100):
        total_flashes += timestep(octopus_map)
    return total_flashes


def part2(my_input):
    octopus_map = np.array([str_to_ints(s.rstrip()) for s in my_input])
    i = 1
    while True:
        flashes = timestep(octopus_map)
        if flashes == 100:
            return i
        i += 1
