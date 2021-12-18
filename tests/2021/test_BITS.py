import pytest

from AoC2021.BITS import BITS


@pytest.mark.parametrize("data, version", [
    ("D2FE28", 6),
    ("38006F45291200", 1)
])
def test_get_version(data, version):
    assert BITS(data).version == version


@pytest.mark.parametrize("data, type_id", [
    ("D2FE28", 4),
    ("38006F45291200", 6)
])
def test_get_type_id(data, type_id):
    assert BITS(data).type_id == type_id


@pytest.mark.parametrize("data, package_length", [
    ("38006F45291200", 27)
])
def test_get_package_length(data, package_length):
    assert BITS(data).package_length == package_length


@pytest.mark.parametrize("data, sub_package_count", [
    ("38006F45291200", 2),
    ("EE00D40C823060", 3)
])
def test_get_sub_package_count(data, sub_package_count):
    assert len(BITS(data).sub_packets) == sub_package_count


def test_sub_packet_values1():
    bits = BITS("EE00D40C823060")
    assert bits.sub_packets[0].get_value() == 1
    assert bits.sub_packets[1].get_value() == 2
    assert bits.sub_packets[2].get_value() == 3


def test_sub_packet_values2():
    bits = BITS("38006F45291200")
    assert bits.sub_packets[0].get_value() == 10
    assert bits.sub_packets[1].get_value() == 20


def test_get_value():
    assert BITS("D2FE28").get_value() == 2021


@pytest.mark.parametrize("data, version_sum", [
    ("8A004A801A8002F478", 16),
    ("620080001611562C8802118E34", 12),
    ("C0015000016115A2E0802F182340", 23),
    ("A0016C880162017C3686B18A3D4780", 31),
])
def test_get_version_sum(data, version_sum):
    assert BITS(data).get_version_sum() == version_sum
