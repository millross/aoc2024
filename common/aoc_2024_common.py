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