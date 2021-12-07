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
    ("02", 2, "inputs/input02.txt",         1942068080),
    ("03", 1, "inputs/input03_test.txt",    198),
    ("03", 1, "inputs/input03.txt",         852500),
    ("03", 2, "inputs/input03_test.txt",    230),
    ("03", 2, "inputs/input03.txt",         1007985),
    ("04", 1, "inputs/input04_test.txt",    4512),
    ("04", 1, "inputs/input04.txt",         67716),
    ("04", 2, "inputs/input04_test.txt",    1924),
    ("04", 2, "inputs/input04.txt",         1830),
    ("05", 1, "inputs/input05_test.txt",    5),
    ("05", 1, "inputs/input05.txt",         4826),
    ("05", 2, "inputs/input05_test.txt",    12),
    ("05", 2, "inputs/input05.txt",         16793),
    ("06", 1, "inputs/input06_test.txt",    5934),
    ("06", 1, "inputs/input06.txt",         388419),
    ("06", 2, "inputs/input06_test.txt",    26984457539),
    ("06", 2, "inputs/input06.txt",         1740449478328),
    ("07", 1, "inputs/input07_test.txt",    37),
    ("07", 1, "inputs/input07.txt",         342730),
    ("07", 2, "inputs/input07_test.txt",    168),
    ("07", 2, "inputs/input07.txt",         92335207),
])
def test_everything(day, part, inputfile, result):
    module = importlib.import_module(f"AoC2021.day{day}")
    with open("tests/2021/" + inputfile) as file:
        myinput = file.readlines()
    if part == 1:
        assert(module.part1(myinput) == result)
    else:
        assert(module.part2(myinput) == result)
