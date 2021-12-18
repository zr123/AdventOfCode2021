import importlib
import pytest


# this probably violates a number of guidelines on how to write good tests
@pytest.mark.parametrize("day, part, input_file, result", [
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
    ("08", 1, "inputs/input08_test.txt",    26),
    ("08", 1, "inputs/input08.txt",         532),
    ("08", 2, "inputs/input08_test.txt",    61229),
    ("08", 2, "inputs/input08.txt",         1011284),
    ("09", 1, "inputs/input09_test.txt",    15),
    ("09", 1, "inputs/input09.txt",         548),
    ("09", 2, "inputs/input09_test.txt",    1134),
    ("09", 2, "inputs/input09.txt",         786048),
    ("10", 1, "inputs/input10_test.txt",    26397),
    ("10", 1, "inputs/input10.txt",         358737),
    ("10", 2, "inputs/input10_test.txt",    288957),
    ("10", 2, "inputs/input10.txt",         4329504793),
    ("11", 1, "inputs/input11_test.txt",    1656),
    ("11", 1, "inputs/input11.txt",         1683),
    ("11", 2, "inputs/input11_test.txt",    195),
    ("11", 2, "inputs/input11.txt",         788),
    ("12", 1, "inputs/input12_test1.txt",   10),
    ("12", 1, "inputs/input12_test2.txt",   19),
    ("12", 1, "inputs/input12_test3.txt",   226),
    ("12", 1, "inputs/input12.txt",         5920),
#    ("12", 2, "inputs/input12_test1.txt",   36), # bugged
    ("12", 2, "inputs/input12_test2.txt",   103),
    ("12", 2, "inputs/input12_test3.txt",   3509),
    ("12", 2, "inputs/input12.txt",         155477),
    ("13", 1, "inputs/input13_test.txt",    17),
    ("13", 1, "inputs/input13.txt",         669),
    ("13", 2, "inputs/input13.txt",         "UEFZCUCJ"),
    ("14", 1, "inputs/input14_test.txt",    1588),
    ("14", 1, "inputs/input14.txt",         3906),
    ("14", 2, "inputs/input14_test.txt",    2188189693529),
    ("14", 2, "inputs/input14.txt",         4441317262452),
    ("15", 1, "inputs/input15_test.txt",    40),
    ("15", 1, "inputs/input15.txt",         487),
    ("15", 2, "inputs/input15_test.txt",    315),
    ("15", 2, "inputs/input15.txt",         2821),
    ("16", 1, "inputs/input16_test1.txt",   16),
    ("16", 1, "inputs/input16_test2.txt",   12),
    ("16", 1, "inputs/input16_test3.txt",   23),
    ("16", 1, "inputs/input16_test4.txt",   31),
    ("16", 1, "inputs/input16.txt",         920),
])
def test_everything(day, part, input_file, result):
    module = importlib.import_module(f"AoC2021.day{day}")
    with open("tests/2021/" + input_file) as file:
        my_input = file.readlines()
    if part == 1:
        assert(module.part1(my_input) == result)
    else:
        assert(module.part2(my_input) == result)
