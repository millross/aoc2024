from dataclasses import dataclass
from typing import Optional

from common.aoc_2024_common import load_file

TEST_FILE_NAME = "day6_test_input.txt"
ACTUAL_FILE_NAME = "day6_actual_input.txt"

@dataclass(frozen=True)
class Direction:
    x_unit: int
    y_unit: int

@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def moved(self, direction: Direction, units: int = 1):
        return Position(x=self.x + (direction.x_unit * units), y=self.y + (direction.y_unit * units))


UP = Direction(x_unit=0, y_unit=-1)
DOWN = Direction(x_unit=0, y_unit=1)
LEFT  = Direction(x_unit=-1, y_unit=0)
RIGHT  = Direction(x_unit=1, y_unit=0)

RIGHT_TURN_RESULTS = {
    UP: RIGHT,
    DOWN: LEFT,
    LEFT: UP,
    RIGHT: DOWN
}

class SituationMap:

    def __parse_lines__(self, lines: [str]):
        obstructions: {Position} = set()
        guard_starting_position: Optional[Position] = None
        for y, line in enumerate(lines):
            for x in range(0, len(lines[y])):
                if lines[y][x] == "#":
                    obstructions.add(Position(x, y))
                if lines[y][x] == "^":
                    guard_starting_position = Position(x, y)

        return obstructions, guard_starting_position

    def __init__(self, filename: str):
        lines = load_file(filename)
        self.height: int = len(lines)
        self.width: int = len(lines[0])
        self.obstructions, self.guard_start = self.__parse_lines__(lines)

    def is_obstructed(self, p: Position) -> bool:
        return p in self.obstructions

    def is_outside_map(self, p: Position):
        return p.x not in range(0, self.width) or p.y not in range(0, self.height)

class GuardWalk:

    def __init__(self, situation_map: SituationMap):
        self.sit_map: SituationMap = situation_map
        self.current_position: Position = situation_map.guard_start
        self.visited: {Position} = {self.current_position}
        self.direction: Direction = UP

    def __repr__(self):
        representation: str = ""
        for y in range(0, self.sit_map.height):
            for x in range (0, self.sit_map.width):
                position: Position = Position(x, y)
                if position in self.visited:
                    representation += "X"
                elif self.sit_map.is_obstructed(position):
                    representation += "#"
                else:
                    representation += "."
            representation += "\n"

        return representation

    def __next_proposed_position__(self) -> Position:
        return self.current_position.moved(direction=self.direction)

    def execute_walk(self) -> int:
        left_map: bool = False
        while not left_map:
            self.visited.add(self.current_position)
            proposed_next_position = self.__next_proposed_position__()
            if not (self.sit_map.is_obstructed(proposed_next_position) or
                    self.sit_map.is_outside_map(proposed_next_position)):
                self.current_position = proposed_next_position

            if self.sit_map.is_obstructed(proposed_next_position):
                # We're obstructed so turn right without incrementing visted count
                self.direction = RIGHT_TURN_RESULTS[self.direction]

            if self.sit_map.is_outside_map(proposed_next_position):
                left_map = True

        return len(self.visited)

walk: GuardWalk = GuardWalk(SituationMap(TEST_FILE_NAME))
test_walk_result = walk.execute_walk()
print("Test Part 1 Result " + str(test_walk_result))
actual_walk_result = GuardWalk(SituationMap(ACTUAL_FILE_NAME)).execute_walk()
print("Actual Part 1 Result " + str(actual_walk_result))