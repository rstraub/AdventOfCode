from aoc2024.day01 import total_distance


def test_day_one():
    distance = total_distance("aoc2024/tests/day01.txt")
    assert distance == 11
