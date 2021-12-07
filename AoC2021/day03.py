import numpy as np
import pandas as pd


def str_to_ints(string):
    return [int(char) for char in string]


def part1(my_input):
    numpy_input = np.array([str_to_ints(s.rstrip()) for s in my_input])
    gamma = ""
    epsilon = ""
    for i in range(len(my_input[0]) - 1):
        bit = round(np.sum(numpy_input[:, i]) / len(my_input))
        gamma += str(bit)
        epsilon += str(int(not bit))
    return int(gamma, 2) * int(epsilon, 2)


def part2(my_input):
    pandas_input = pd.DataFrame([str_to_ints(s.rstrip()) for s in my_input])
    # oxygen
    pandas_oxygen = pandas_input.copy()
    for i in range(len(pandas_oxygen.columns)):
        if len(pandas_oxygen) == 1:
            break
        fraction = pandas_oxygen[i].sum() / len(pandas_oxygen)
        if fraction == 0.5:
            bit = 1
        else:
            bit = round(fraction)
        pandas_oxygen = pandas_oxygen[pandas_oxygen[i] == bit]
    oxygen = int("".join([str(s) for s in pandas_oxygen.iloc[0]]), 2)

    pandas_co2 = pandas_input.copy()
    for i in range(len(pandas_co2.columns)):
        if len(pandas_co2) == 1:
            break
        fraction = pandas_co2[i].sum() / len(pandas_co2)
        if fraction == 0.5:
            bit = 0
        else:
            bit = round(1 - fraction)
        pandas_co2 = pandas_co2[pandas_co2[i] == bit]
    co2 = int("".join([str(s) for s in pandas_co2.iloc[0]]), 2)

    return oxygen * co2
