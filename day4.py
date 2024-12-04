from common.aoc_2024_common import load_file,
from typing import Tuple

DIRECTIONS: [Tuple[int,int]] = [[-1,-1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]

class Grid:

    def __init__(self, filename):
        self._lines:[str] = load_file(filename)

    def height(self) -> int:
        return len(self._lines)

    def width(self) -> int:
        return len(self._lines[0])

    def char_at(self, x, y) -> str:
        if x < 0 or x >= self.width():
            return "."
        if y < 0 or y >= self.height():
            return "."
        return self._lines[y][x]

class CandidateAssessor()

class Searcher:

    def __init__(self, grid: Grid, word: str):
        self._grid = grid
        self._word = word


    def count_instances:
