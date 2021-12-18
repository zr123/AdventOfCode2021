import re
import math


def find_first_explodable(snailfish_number):
    nested_counter = 0
    for i, char in enumerate(snailfish_number):
        if char == "[":
            nested_counter += 1
        if char == "]":
            nested_counter -= 1
        if nested_counter == 5:
            break

    if i == len(snailfish_number) - 1:
        return None
    return i


def try_explode(snailfish_number):
    nested_counter = 0
    for i, char in enumerate(snailfish_number):
        if char == "[":
            nested_counter += 1
        if char == "]":
            nested_counter -= 1
        if nested_counter == 5:
            break

    if i == len(snailfish_number)-1:
        return None

    # get nesting
    r = re.compile("^\[(\d+),(\d+)\]")
    m = r.search(snailfish_number[i:])
    left_number, right_number = m.groups()
    snailfish_number = snailfish_number[:i] + r.sub("0", snailfish_number[i:], count=1)

    # increase rightmost number
    r = re.compile(r"(\d+)")
    m = r.search(snailfish_number[i+1:])
    if m is not None:
        number = int(m.group(0))
        number += int(right_number)
        snailfish_number = snailfish_number[:i+1] + r.sub(str(number), snailfish_number[i+1:], count=1)

    # increase leftmost number
    r = re.compile(r"^.*(\d+)")
    m = r.match(snailfish_number[:i])
    if m is not None:
        number = int(m.group(1))
        number += int(left_number)
        snailfish_number = snailfish_number[:m.span(1)[0]] + str(number) + snailfish_number[m.span(1)[1]:]

    return snailfish_number


def find_first_splitable(snailfish_number):
    r = re.compile(r"\d\d")
    m = r.search(snailfish_number)
    if m is not None:
        return m.span()[0]
    return None


def try_split(snailfish_number):
    r = re.compile(r"\d\d")
    m = r.search(snailfish_number)
    if m is not None:
        number = int(m.group())
        insertion = f"[{str(number // 2)},{math.ceil(number / 2)}]"
        snailfish_number = snailfish_number[:m.span()[0]] + insertion + snailfish_number[m.span()[1]:]
        return snailfish_number
    return None


def reduce_old(snailfish_number):
    while True:
        exploded_number = try_explode(snailfish_number)
        if exploded_number is not None:
            snailfish_number = exploded_number
            print(snailfish_number)
            continue

        split_number = try_split(snailfish_number)
        if split_number is not None:
            snailfish_number = split_number
            print(snailfish_number)
            continue

        return snailfish_number



def reduce(snailfish_number):
    while True:
        explosion_i = find_first_explodable(snailfish_number)
        split_i = find_first_splitable(snailfish_number)

        #if explosion_i is not None and split_i is not None:
        #    if explosion_i <= split_i:
        #        snailfish_number = try_explode(snailfish_number)
        #    else:
        #        snailfish_number = try_split(snailfish_number)
        #    continue

        exploded_number = try_explode(snailfish_number)
        if exploded_number is not None:
            snailfish_number = exploded_number
            #print(snailfish_number)
            continue

        split_number = try_split(snailfish_number)
        if split_number is not None:
            snailfish_number = split_number
            #print(snailfish_number)
            continue

        return snailfish_number


def combine(snailfish_nunber1, snailfish_nunber2):
    return f"[{snailfish_nunber1},{snailfish_nunber2}]"


def part1(my_input):
    snailfish_sum = my_input[0].rstrip()
    for snailfish_number in my_input[1:]:
        snailfish_sum = combine(snailfish_sum, snailfish_number.rstrip())
        snailfish_sum = reduce(snailfish_sum)
        print(snailfish_sum)


def part2(my_input):
    pass


if __name__ == '__main__':
    with open("../tests/2021/inputs/input18_test4.txt") as file:
        my_input = file.readlines()

    part1(my_input)
