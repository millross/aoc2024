from common.aoc_2024_common import Position,Direction,Grid, load_file

TEST_FILE_NAME_1: str = "day10_test_input_1.txt"
DIRECTIONS: [Direction] = [Direction(x_unit=0, y_unit=-1),
              Direction(x_unit=1, y_unit=0),
              Direction(x_unit=0, y_unit=1),
              Direction(x_unit=-1, y_unit=0)]

MIN_HEIGHT: int = 0
TARGET_HEIGHT: int = 9

def get_path_candidates():


class HeightMap(Grid):

    def height_at(self, p: Position):
        c = self.char_at(p)
        try:
            return int(c)
        except ValueError:
            return -1

    def get_positions_for_height(self, height: int):
        positions: {Position} = set()
        for y in range(0, self.height()):
            for x in range(0, self.width()):
                candidate_position = Position(x=y, y=y)
                if self.height_at(candidate_position) == height:
                    positions.add(candidate_position)
        return positions

class HikingPathsFinder:

    def __init__(self, height_map: HeightMap):
        self.height_map = height_map

    def __get_potential_trail_positions_for_height(self, height: int):


    def find_trail_ends(self):
        # Create a sparse data structure for positions of each height which can be part of a trail
        # This means for height 0, at least one neighbour in any direction of height 1
        # For height 9, at least one neighbour in any direction of height 8
        # For any other height h, at least one neightbour of height h-1 and at least one of height h+1
        # Any other positions cannot possibly be part of a hiking trail


def part_1_count_hiking_trails(grid: HeightMap) -> int:
    return 0

def next_positions(height_map: HeightMap, height: int, position: Position) -> [Position]:
    positions_to_check = map(lambda d: position.moved(d, 1), DIRECTIONS)
    next_positions = list(filter(position))

def part_1(filename: str) -> int:
    lines = load_file(TEST_FILE_NAME_1)
    grid = HeightMap(lines)
    return part_1_count_hiking_trails(grid)

assert part_1(TEST_FILE_NAME_1) == 1