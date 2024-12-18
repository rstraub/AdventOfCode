def calculate_number_of_safe_reports(reports) -> int:
    return sum(map(report_is_safe, reports))


def report_is_safe(report: tuple[int, ...]) -> bool:
    left_levels = report[:-1]
    right_levels = report[1:]
    combinations = zip(left_levels, right_levels)

    diffs = [right - left for left, right in combinations]
    within_safe_range = all(in_safe_range(diff) for diff in diffs)
    all_increasing = all(diff > 0 for diff in diffs)
    all_decreasing = all(diff < 0 for diff in diffs)

    return within_safe_range and (all_increasing or all_decreasing)


def in_safe_range(diff: int) -> bool:
    return 1 <= abs(diff) <= 3


def calculate_number_of_safe_reports_from_unparsed(reports: str) -> int:
    parsed = parse_reports(reports)
    return calculate_number_of_safe_reports(parsed)


def parse_reports(reports: str):
    result = []

    lines = reports.split("\n")
    for line in lines:
        cleaned = line.strip()

        levels = tuple([int(level) for level in cleaned.split(" ")])

        result.append(levels)

    return tuple(result)
