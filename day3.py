from common.aoc_2024_common import read_file
import re

TEST_FILE_NAME = "day3_test_input.txt"
ACTUAL_FILE_NAME = "day3_actual_input.txt"
MUL_REGEX_PATTERN = r"mul\(\d+,\d+\)"
MUL_CALL_REGEX_PATTERN="mul\((?P<left>\d+),(?P<right>\d+)\)"

def evaluate_mul(mul_call: str):
    match = re.search(MUL_CALL_REGEX_PATTERN, mul_call)
    left: int = int(match.group("left"))
    right:int  = int(match.group("right"))
    return left * right

def sum_muls(input: str) -> int:
    mul_calls = re.findall(MUL_REGEX_PATTERN, input)
    return sum(map(evaluate_mul, mul_calls))

def from_first_do(candidate: str):
    return candidate.split("do()", 1)[1]

def apply_conditionals(input: str) -> [str]:
    # replace all characters which fall between "don't()" and "do() (including "do and don't" with a .
    # find first index of 'don't' and work from there
    splits = filter(lambda s: "do()" in s, ("do()" + input).split("don't"))
    # Extract any which don't contain a do() marker as they are entirely covered by don't
    active_blocks = list(map(from_first_do, splits))
    return active_blocks

def part_1(filename:str) -> int:
    return sum_muls(read_file(filename))

def part_2(filename:str) -> int:
    base_input = read_file(filename)
    corrected_inputs = apply_conditionals(base_input)
    print (corrected_inputs)
    sums = map(sum_muls, corrected_inputs)
    return sum(sums)

print("Part 1 test result: " + str(part_1(TEST_FILE_NAME)))
print("Part 1 actual result: " + str(part_1(ACTUAL_FILE_NAME)))
print("Part 2 test result: " + str(part_2(TEST_FILE_NAME)))
print("Part 2 actual result: " + str(part_2(ACTUAL_FILE_NAME)))
