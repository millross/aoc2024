from common.aoc_2024_common import load_file
import re
from collections import Counter

TEST_FILE_NAME: str = "day_1_test_input"
ACTUAL_FILE_NAME: str  = "day_1_input_1.txt"
LINE_REGEX: str = "\s*(?P<left>\d+)\s*(?P<right>\d+)"
LEFT: str = "left"
RIGHT: str = "right"

def _extract_list(lines, side: str) -> list[int]:
    matches = map(lambda l: re.search(LINE_REGEX, l), lines)
    return list(map(lambda m: int(m.group(side)), matches))

def _load_lists(file_name):
    lines = load_file(file_name)
    left = _extract_list(lines, LEFT)
    right = _extract_list(lines, RIGHT)
    return left, right


def part_1(file_name: str) -> int:
    left, right = _load_lists(file_name)
    left.sort()
    right.sort()
    zipped = list(zip(left, right))
    return sum(map(lambda t: abs(t[0] - t[1]), zipped))

def get_count_of(counts: dict, value: int) -> int:
    return counts.get(value, 0)

def part_2(file_name: str) -> int:
    left, right = _load_lists(file_name)
    counts = Counter(right)
    return sum(map(lambda v: v * counts.get(v, 0), left))



print("Test result " + str(part_1(TEST_FILE_NAME)))
print("Actual result " + str(part_1(ACTUAL_FILE_NAME)))
print("Test result 2 " + str(part_2(TEST_FILE_NAME)))
print("Actual result 2 " + str(part_2(ACTUAL_FILE_NAME)))

