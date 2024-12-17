import pytest

from aoc2024.day02 import calculate_number_of_safe_reports, report_is_safe


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


@pytest.mark.parametrize("report", [(7, 6, 4, 2, 1), (1, 3, 6, 7, 9)])
def test_report_is_safe_when_level_diffs_between_one_and_three(report: tuple[int, ...]):
    assert report_is_safe(report)


@pytest.mark.parametrize("report", [(1, 2, 7, 8, 9), (9, 7, 6, 2, 1)])
def test_report_is_unsafe_when_level_diffs_exceeds_three(report: tuple[int, ...]):
    assert not report_is_safe(report)


def test_report_is_unsafe_when_level_diffs_increase_and_decrease():
    assert not report_is_safe((1, 3, 2, 4, 5))


def test_report_is_unsafe_when_level_diffs_are_stable():
    assert not report_is_safe((8, 6, 4, 4, 1))
