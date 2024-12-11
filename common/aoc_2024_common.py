from dataclasses import dataclass
import itertools as it

def load_file(filename):
    loaded = list()

    input_file = open(filename)
    for (line) in input_file:
        loaded.append(line.rstrip())
    input_file.close()
    return loaded

def read_file(filename: str) -> str:
    loaded = ""
    input_file = open(filename)
    for (line) in input_file:
        loaded = loaded + line.rstrip()
    input_file.close()
    return loaded

def group_by_delimiter(lines_list, delimiter) -> [[str]]:
    return  [list(group) for key, group in it.groupby(lines_list, lambda s: s == delimiter) if not key]

@dataclass(frozen=True)
class Direction:
    x_unit: int
    y_unit: int

@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def moved(self, dir: Direction, units: int = 1):
        return Position(x=self.x + (dir.x_unit * units), y=self.y + (dir.y_unit * units))

@dataclass(frozen=True)
class Grid:

    lines:[str]
    default_char: str = "."

    def height(self) -> int:
        return len(self.lines)

    def width(self) -> int:
        return len(self.lines[0])

    def char_at(self, position: Position) -> str:
        if position.x < 0 or position.x >= self.width():
            return self.default_char
        if position.y < 0 or position.y >= self.height():
            return self.default_char
        return self.lines[position.y][position.x]
