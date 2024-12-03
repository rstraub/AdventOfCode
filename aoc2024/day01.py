#!/usr/bin/env python3
import sys


def total_distance(path: str) -> int:
    contents = read_contents(path)
    lists = parse_lists(contents)

    return calculate_total_distance(lists)


def read_contents(path: str) -> list[str]:
    contents = []
    with open(path, "r") as f:
        lines = f.readlines()
        for line in lines:
            contents.append(line.replace("\n", ""))
    return contents


def parse_lists(input):
    left_list = []
    right_list = []

    for line in input:
        left_list.append(line.split("   ")[0])
        right_list.append(line.split("   ")[1])

    return (left_list, right_list)


def calculate_total_distance(lists):
    return -1


if __name__ == "__main__":
    file_path = sys.argv[1]
    print(total_distance(file_path))
