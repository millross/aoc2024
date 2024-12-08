import itertools as it

from typing import Callable
from common.aoc_2024_common import load_file, group_by_delimiter
from math import floor
from functools import cmp_to_key

TEST_FILE_NAME: str = "day5_test_input.txt"
ACTUAL_FILE_NAME: str = "day5_actual_input.txt"

def load_file_inputs(file_name: str) -> [[str], [str]]:
    groups: [str] = group_by_delimiter(load_file(file_name), "")
    return groups[0], groups[1]


# Represents single "page x must appear before page y" specification
class OrderingRuleDefinition:

    def __init__(self, raw_rule: str):
        page_numbers = raw_rule.split("|")
        if len(page_numbers) > 2:
            raise Exception("Only expecting two numbers in OrderingRule but saw " + raw_rule)
        self.before, self.after = int(page_numbers[0]), int(page_numbers[1])

    def __repr__(self):
        return str(self.before) + " must precede " + str(self.after)


# Represents easy to interrogate "given a page number x and a page number y, is their relative order compliant"
# specification, compiled from OrderingRuleDefinitions
class OrderingSpecification:

    def __init__(self, ordering_rules: [OrderingRuleDefinition]):
        ordering_rules.sort(key=lambda d: d.before)
        self.specification = {}
        for k, g in it.groupby(ordering_rules, lambda r: r.before):
            self.specification[k] = set(map(lambda r: r.after, g))

    def is_compliant(self, earlier: int, later: int):
        # for x in self.specification:
        #     print(x, self.specification[x])
        must_be_after_later = self.specification.get(later, set())
        # if later not in self.specification:
        #     return True
        return earlier not in must_be_after_later

def page_ordering_complies_with_specification(ordering: [int], specification: OrderingSpecification) -> bool:
    # Iterate through pairs of consecutive elements in ordering until we get a False result
    for earlier,later in zip(ordering, ordering[1:]):
        if not specification.is_compliant(earlier=earlier, later=later):
            return False
    return True

def convert_ordering_str_to_list(ordering: str) -> [int]:
    return list(map(int, ordering.split(",")))

def middle_page_number(ordering: [int]) -> int:
    return ordering[floor(len(ordering) / 2)]

def load_orderings_and_specification(file_name: str) -> [OrderingSpecification, [[int]]]:
    ordering_rules: str
    page_orderings_strs: str
    [ordering_rules, page_orderings_strs] = load_file_inputs(file_name)
    page_orderings: [[int]] = list(map(convert_ordering_str_to_list, page_orderings_strs))
    ordering_specification: OrderingSpecification = OrderingSpecification(list(map(OrderingRuleDefinition, ordering_rules)))
    return ordering_specification, page_orderings

def part_1(file_name):
    ordering_specification, page_orderings = load_orderings_and_specification(file_name)
    compliant_orderings = filter(lambda o: page_ordering_complies_with_specification(o, ordering_specification), page_orderings)
    middle_page_numbers = map(middle_page_number, compliant_orderings)
    return sum(middle_page_numbers)

def specified_ordering_compare(ordering_rules: dict[int, set[int]], left: int, right: int):
    must_appear_before: [int] = ordering_rules.get(left, [])
    if right in must_appear_before:
        return -1
    else:
        if left in ordering_rules.get(right, []):
            return 1
    # Not sure that this should happen but neither must appear before the other so we're good
    return 0

def specified_ordering_comparator(ordering_rules: dict[int, set[int]]) -> Callable[[int, int], int]:
    return lambda l, r: specified_ordering_compare(ordering_rules=ordering_rules, left=l, right=r)

def fix_ordering(ordering: [int], spec:dict[int, set[int]]):
    return sorted(ordering, key=cmp_to_key(specified_ordering_comparator(spec)))

def part_2(file_name):
    ordering_specification, page_orderings = load_orderings_and_specification(file_name)
    ordering_specification, page_orderings = load_orderings_and_specification(file_name)
    non_compliant_orderings = list(filter(lambda o: not page_ordering_complies_with_specification(o, ordering_specification), page_orderings))

    fixed_page_orderings = map(lambda ordering: fix_ordering(ordering=ordering, spec=ordering_specification.specification), non_compliant_orderings)
    middle_values = map(middle_page_number, fixed_page_orderings)
    return sum(middle_values)

def test_compliance():
    [ordering_rules, page_orderings] = load_file_inputs(TEST_FILE_NAME)
    ordering_specification: OrderingSpecification = OrderingSpecification(list(map(OrderingRuleDefinition, ordering_rules)))
    print(ordering_specification.is_compliant(earlier=13, later=29))

print("Part 1 test result: " + str(part_1(TEST_FILE_NAME)))
print("Part 1 actual result: " + str(part_1(ACTUAL_FILE_NAME)))

print("Part 2 test result: " + str(part_2(TEST_FILE_NAME)))
print("Part 2 actual result: " + str(part_2(ACTUAL_FILE_NAME)))
