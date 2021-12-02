import numpy as np
import importlib
import pytest

# this probably violates a number of guidelines on how to write good tests
@pytest.mark.parametrize("day, part, inputfile, result", [
    ("01", 1, "inputs/input01_test.txt",    7),
    ("01", 1, "inputs/input01.txt",         1374),
    ("01", 2, "inputs/input01_test.txt",    5),
    ("01", 2, "inputs/input01.txt",         1418),
    ("02", 1, "inputs/input02_test.txt",    150),
    ("02", 1, "inputs/input02.txt",         2039912),
    ("02", 2, "inputs/input02_test.txt",    900),
    ("02", 12, "inputs/input02.txt",        1942068080),
])
def test_everything(day, part, inputfile, result):
    module = importlib.import_module(f"AoC2021.day{day}")
    with open("tests/2021/" + inputfile) as file:
        myinput = file.readlines()
    if part == 1:
        assert(module.part1(myinput) == result)
    else:
        assert(module.part2(myinput) == result)
