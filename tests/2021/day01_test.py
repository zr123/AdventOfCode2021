import numpy as np
import importlib
import pytest

# this probably violates a number of guidelines on how to write good tests
@pytest.mark.parametrize("day, part, inputfile, result", [
    ("01", 1, "inputs/input01_test.txt",    7),
    ("01", 1, "inputs/input01.txt",         1374),
    ("01", 2, "inputs/input01_test.txt",    5),
    ("01", 2, "inputs/input01.txt",         1418)
])
def test_everything(day, part, inputfile, result):
    module = importlib.import_module(f"AoC2021.day{day}")
    myinput = np.loadtxt("tests/2021/" + inputfile)
    if part == 1:
        assert(module.part1(myinput) == result)
    else:
        assert(module.part2(myinput) == result)
