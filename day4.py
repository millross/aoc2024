from common.aoc_2024_common import load_file, Direction, Position
from typing import Tuple

DIRECTIONS: [Direction] = [Direction(-1, -1), Direction(0, -1), Direction(1, -1),
                           Direction(-1, 0), Direction(1, 0),
                           Direction(-1, 1), Direction(0, 1), Direction(1, 1)]
TARGET: str = "XMAS"

class Grid:

    def __init__(self, filename):
        self._lines:[str] = load_file(filename)

    def height(self) -> int:
        return len(self._lines)

    def width(self) -> int:
        return len(self._lines[0])

    def char_at(self, position: Position) -> str:
        if position.x < 0 or position.x >= self.width():
            return "."
        if position.y < 0 or position.y >= self.height():
            return "."
        return self._lines[position.y][position.x]

class CandidateAssessor:
    def __init__(self, grid: Grid, position: Position):
        self.grid = grid
        self.position = position

    def __check_in_direction_(self, direction: Direction) -> bool:
        for i in range(0, len(TARGET)):
            c = self.grid.char_at(self.position.moved(direction, i))
            if c != TARGET[i]:
                return False
        return True

    # Count how many "XMAS"s start from this position
    def check(self) -> int:
        if self.grid.char_at(self.position) != TARGET[0]:
            return 0
        # Test all directions from this position
        results
        DIRECTIONS.map(lambda d:)

class Searcher:

    def __init__(self, grid: Grid, word: str):
        self._grid = grid
        self._word = word


    def count_instances:
