import numpy as np


def str_to_ints(string):
    return [int(char) for char in string]


def calc_risk_level(x_coord, y_coord, risk_levels, risk_map):
    risks = []
    if x_coord > 0:
        risks.append(risk_levels[y_coord, x_coord - 1])
    if x_coord < risk_levels.shape[1] - 1:
        risks.append(risk_levels[y_coord, x_coord + 1])
    if y_coord > 0:
        risks.append(risk_levels[y_coord - 1, x_coord])
    if y_coord < risk_levels.shape[0] - 1:
        risks.append(risk_levels[y_coord + 1, x_coord])

    return min(risks) + risk_map[y_coord, x_coord]


def calcuate_risk_levels(risk_map):
    risk_levels = np.full(risk_map.shape, 2 ** 30)
    risk_levels[0, 0] = 0

    loop_var = True
    iteration = 0
    while loop_var:
        previous_risk_levels = risk_levels.copy()
        # recalculate values for every location
        for n in range(2, sum(risk_levels.shape)):
            for i in range(n):
                x = i
                y = (n - 1) - i
                if x >= risk_levels.shape[1] or y >= risk_levels.shape[0]:
                    continue
                risk_levels[y, x] = calc_risk_level(x, y, risk_levels, risk_map)

        # stop recalculating the risk levels if there are no more changes
        print(iteration)
        iteration += 1
        if (previous_risk_levels == risk_levels).all():
            loop_var = False

    return risk_levels


def part1(my_input):
    risk_map = np.array([str_to_ints(s.rstrip()) for s in my_input])
    risk_levels = calcuate_risk_levels(risk_map)
    return risk_levels[-1, -1]


def bloat_risk_map(risk_map, factor=5):
    bloated_risk_map = np.zeros((risk_map.shape[0] * factor, risk_map.shape[1] * factor))

    for x in range(factor):
        for y in range(factor):
            intermediate_risk_map = risk_map.copy()
            intermediate_risk_map += x + y
            intermediate_risk_map[intermediate_risk_map > 9] -= 9
            bloated_risk_map[
                risk_map.shape[0] * y: risk_map.shape[0] * (y + 1),
                risk_map.shape[1] * x: risk_map.shape[1] * (x + 1)
            ] = intermediate_risk_map

    return bloated_risk_map


def part2(my_input):
    risk_map = np.array([str_to_ints(s.rstrip()) for s in my_input])
    risk_map = bloat_risk_map(risk_map)
    risk_levels = calcuate_risk_levels(risk_map)
    return risk_levels[-1, -1]
