from dataclasses import dataclass
from itertools import count

from common.aoc_2024_common import load_file, Direction, Position
from typing import Tuple

DIRECTIONS: [Direction] = [Direction(-1, -1), Direction(0, -1), Direction(1, -1),
                           Direction(-1, 0), Direction(1, 0),
                           Direction(-1, 1), Direction(0, 1), Direction(1, 1)]
TARGET: str = "XMAS"
TEST_FILE_NAME = "day4_test_input.txt"
ACTUAL_FILE_NAME = "day4_actual_input.txt"

@dataclass(frozen=True)
class Grid:

    lines:[str]

    def height(self) -> int:
        return len(self.lines)

    def width(self) -> int:
        return len(self.lines[0])

    def char_at(self, position: Position) -> str:
        if position.x < 0 or position.x >= self.width():
            return "."
        if position.y < 0 or position.y >= self.height():
            return "."
        return self.lines[position.y][position.x]

class CandidateAssessor:
    def __init__(self, grid: Grid, position: Position) -> None:
        self.grid = grid
        self.position = position

    def __check_in_direction__(self, direction: Direction) -> bool:
        for i in range(0, len(TARGET)):
            c = self.grid.char_at(self.position.moved(direction, i))
            if c != TARGET[i]:
                return False
        return True

    # Count how many "XMAS"s start from this position
    def count_instances(self) -> int:
        if self.grid.char_at(self.position) != TARGET[0]:
            return 0
        # Test all directions from this position
        return sum(1 for _ in filter(lambda b: b, map(lambda d: self.__check_in_direction__(d), DIRECTIONS)))

@dataclass(frozen=True)
class Searcher:

    grid: Grid
    word: str

    def count_instances(self) -> int:
        instance_count: int = 0
        for y in range(0, self.grid.height()):
            for x in range(0, self.grid.width()):
                assessor: CandidateAssessor = CandidateAssessor(self.grid, Position(x, y))
                instance_count += assessor.count_instances()

        return instance_count

class Part2CandidateAssessor:
    # Look for two "MAS" in shape of an X with A in centre of group of 9

part_1_test_result = Searcher(grid=Grid(load_file(TEST_FILE_NAME)), word=TARGET).count_instances()
print("Part 1 Test result = " + str(part_1_test_result))
part_1_actual_result = Searcher(grid=Grid(load_file(ACTUAL_FILE_NAME)), word=TARGET).count_instances()
print("Part 1 Actual result = " + str(part_1_actual_result))
