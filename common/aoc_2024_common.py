from dataclasses import dataclass


def load_file(filename):
import itertools as it

def load_file(filename) -> [str]:
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


