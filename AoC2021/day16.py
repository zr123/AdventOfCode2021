import numpy as np
from bitarray import bitarray, util

from AoC2021.BITS import BITS


def part1(my_input):
    packet_string = my_input[0].rstrip()
    return BITS(packet_string).get_version_sum()


def part2(my_input):
    pass


if __name__ == '__main__':
    with open("../tests/2021/inputs/inputs16_test1.txt") as file:
        my_input = file.readlines()

    part1(my_input)
