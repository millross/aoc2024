from dataclasses import dataclass


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

@dataclass(frozen=True)
class Direction:
    x_unit: int
    y_unit: int

@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def moved(self, dir: Direction, units: int):
        return Position(x=self.x + (dir.x_unit * units), y=self.y + (dir.y_unit * units))


