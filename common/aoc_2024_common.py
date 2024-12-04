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

@dataclass
class Position:
    x: int
    y: int
