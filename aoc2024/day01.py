def total_distance(path: str) -> int:
    contents = read_contents(path)
    left_list, right_list = parse_lists(contents)

    return calculate_total_distance(left_list, right_list)


def read_contents(path: str) -> list[str]:
    contents = []
    with open(path, "r") as f:
        lines = f.readlines()
        for line in lines:
            contents.append(line.strip())
    return contents


def parse_lists(input):
    left_list = []
    right_list = []

    for line in input:
        left_list.append(int(line.split("   ")[0]))
        right_list.append(int(line.split("   ")[1]))

    return (left_list, right_list)


def calculate_total_distance(left_list, right_list):
    zipped = list(zip(sorted(left_list), sorted(right_list)))

    distances = [abs(right - left) for left, right in zipped]

    return sum(distances)


if __name__ == "__main__":
    file_path = "aoc2024/input/day01.txt"
    print(total_distance(file_path))
