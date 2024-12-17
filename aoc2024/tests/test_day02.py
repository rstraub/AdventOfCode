from aoc2024.day02 import calculate_number_of_safe_reports


def test_calculate_number_of_safe_reports():
    reports = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
    """.strip()

    assert calculate_number_of_safe_reports(reports) == 2

