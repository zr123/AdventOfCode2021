import numpy as np
import re


def get_paper_size(instructions):
    for instruction in instructions:
        m = re.match("^.+x=(\d+)$", instruction)
        if m is not None:
            x_size = int(m.group(1))
            break

    for instruction in instructions:
        m = re.match("^.+y=(\d+)$", instruction)
        if m is not None:
            y_size = int(m.group(1))
            break

    return y_size*2+1, x_size*2+1


def read_instructions(my_input):
    x_array = []
    y_array = []
    instructions = []
    for line in my_input:
        line = line.rstrip()
        if len(line) == 0:
            continue
        if not line.startswith("fold along"):
            x, y = line.split(",")
            x_array.append(int(x))
            y_array.append(int(y))
        else:
            instructions.append(line)

    y_size, x_size,  = get_paper_size(instructions)
    paper = np.zeros((y_size, x_size), dtype=int)
    for x, y in zip(x_array, y_array):
        paper[y, x] = 1

    return paper, instructions


def fold_paper(paper, instruction):
    # fold along x
    m = re.match("^.+x=(\d+)$", instruction)
    if m is not None:
        foldline = int(m.group(1))
        paper = paper[:, :foldline] + paper[:, -1:foldline:-1]

    # fold along y
    m = re.match("^.+y=(\d+)$", instruction)
    if m is not None:
        foldline = int(m.group(1))
        paper = paper[:foldline, :] + paper[-1:foldline:-1, :]

    paper[paper == 2] = 1
    return paper


def part1(my_input):
    paper, instructions = read_instructions(my_input)
    paper = fold_paper(paper, instructions[0])
    return np.sum(paper)


def print_paper(paper):
    for y in range(paper.shape[0]):
        string = ""
        for x in range(paper.shape[1]):
            if paper[y, x] == 0:
                string += "."
            else:
                string += "#"
        print(string)


def part2(my_input):
    paper, instructions = read_instructions(my_input)

    for instruction in instructions:
        paper = fold_paper(paper, instruction)

    print_paper(paper)
    # Todo conversion "hash text" to string
    return "UEFZCUCJ"


if __name__ == '__main__':
    with open("../tests/2021/inputs/input13.txt") as file:
        my_input = file.readlines()

    part2(my_input)
