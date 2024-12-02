from common.aoc_2024_common import load_file

TEST_FILE_NAME: str = "day2_test_input.txt"
ACTUAL_FILE_NAME: str = "day2_actual_input.txt"

def sign(x: int):
    return int(x/abs(x)) if x != 0 else 0

def is_safe(levels: [int]) -> bool:
    diffs = [later - earlier for earlier, later in zip(levels, levels[1:])]
    for index, diff in enumerate(diffs):
        # Diff 0 = unsafe
        if index > 0 and sign(diff) != sign(diffs[index - 1]):
            return False
        # Diff > 3 is unsafe
        if abs(diff) > 3 or abs(diff) < 1:
            return False
    return True

def remove_at_index(l: [int], index: int) -> [int]:
    return l[:index] + l[index + 1:]

class Level:

    def __init__(self, level_as_str: str):
        self.values = list(map(int, level_as_str.split(" ")))

    def __repr__(self):
        return str(self.values)

    def is_safe(self) -> bool:
        return is_safe(self.values)

    def is_safe_with_dampener(self):
        for dampener_candidate_index in range(0,len(self.values)):
            dampener_candidate = remove_at_index(self.values, dampener_candidate_index)
            if is_safe(dampener_candidate):
                # print("Safe via dampener for " + str(self.values))
                # print("Safe candidate is " + str(dampener_candidate))
                return True
        return False

def load_levels(filename: str) -> list[Level]:
    return list(map(lambda l: Level(l), load_file(filename)))

def part_1(filename: str) -> int:
    levels = load_levels(filename)
    safe_levels = list(filter(lambda l: l.is_safe(), levels))
    return len(safe_levels)

print("Part 1 test result " + str(part_1(TEST_FILE_NAME)))
print("Part 1 actual result " + str(part_1(ACTUAL_FILE_NAME)))

def part_2(filename: str) -> int:
    levels = load_levels(filename)
    safe_levels = list(filter(lambda l: l.is_safe() or l.is_safe_with_dampener(), levels))
    # for level in safe_levels:
    #     print(str(level))
    return len(safe_levels)

print("Part 2 test result " + str(part_2(TEST_FILE_NAME)))
print("Part 2 actual result " + str(part_2(ACTUAL_FILE_NAME)))
