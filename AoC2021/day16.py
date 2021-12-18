from AoC2021.BITS import BITS


def part1(my_input):
    packet_string = my_input[0].rstrip()
    return BITS(packet_string).get_version_sum()


def part2(my_input):
    packet_string = my_input[0].rstrip()
    return BITS(packet_string).get_value()
