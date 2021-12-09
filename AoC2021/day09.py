import numpy as np


def str_to_ints(string):
    return [int(char) for char in string]


def part1(my_input):
    heatmap = np.array([str_to_ints(s.rstrip()) for s in my_input])
    low_points = heatmap[
        (heatmap - np.lib.pad(heatmap[1:, :], ((0, 1), (0, 0)), constant_values=9) < 0) &
        (heatmap - np.lib.pad(heatmap[0:-1, :], ((1, 0), (0, 0)), constant_values=9) < 0) &
        (heatmap - np.lib.pad(heatmap[:, 1:], ((0, 0), (0, 1)), constant_values=9) < 0) &
        (heatmap - np.lib.pad(heatmap[:, 0:-1], ((0, 0), (1, 0)), constant_values=9) < 0)
    ]
    return len(low_points) + np.sum(low_points)


def fill_map(map_array, location, value, stopping_value):
    y, x = location
    if map_array[y, x] in [value, stopping_value]:
        return
    map_array[y, x] = value
    if x > 0:
        fill_map(map_array, (y, x-1), value, stopping_value)
    if x < map_array.shape[1]-1:
        fill_map(map_array, (y, x+1), value, stopping_value)
    if y > 0:
        fill_map(map_array, (y-1, x), value, stopping_value)
    if y < map_array.shape[0]-1:
        fill_map(map_array, (y+1, x), value, stopping_value)


def part2(my_input):
    heatmap = np.array([str_to_ints(s.rstrip()) for s in my_input])
    basin_map = np.zeros(heatmap.shape)
    basin_map[heatmap == 9] = -1

    counter = 1
    for y in range(heatmap.shape[0]):
        for x in range(heatmap.shape[1]):
            if basin_map[y, x] == 0:
                fill_map(basin_map, (y, x), counter, -1)
                counter += 1

    basin_sizes = []
    for i in range(1, counter+1):
        basin_sizes.append(len(basin_map[basin_map == i]))

    basin_sizes = sorted(basin_sizes)
    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]

