from aoc2024.day01 import total_distance, total_similarity


def test_distance_score():
    distance = total_distance("./aoc2024/tests/day01.txt")
    assert distance == 11


def test_similarity_score():
    similarity = total_similarity("./aoc2024/tests/day01.txt")
    assert similarity == 31
