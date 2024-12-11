from common.aoc_2024_common import Position,Direction,Grid, load_file

TEST_FILE_NAME_1: str = "day10_test_input_1.txt"

def part_1_count_hiking_trails(grid: Grid) -> int:
    return 0

def part_1(filename: str) -> int:
    lines = load_file(TEST_FILE_NAME_1)
    grid = Grid(lines)
    return part_1_count_hiking_trails(grid)

assert part_1(TEST_FILE_NAME_1) == 1