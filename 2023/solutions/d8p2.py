import math

def parseInput(filename: str) -> tuple[str, dict[str, list[str]]]:
    with open(filename) as file:
        lines = [line.strip() for line in file.readlines() if line.strip() != '']

    dirs, *paths = lines
    path_dict = dict()
    for path in paths:
        inp, out = path.split(' = ')
        out = out.removeprefix('(').removesuffix(')').split(', ')
        path_dict[inp] = out

    return dirs, path_dict

def findCycleLength(start_node: str, dirs: str, paths: dict[str, list[str]]) -> int:
    count = 0
    cur_dir_idx = 0
    cur_ele = start_node
    while not cur_ele.endswith('Z'):
        count += 1
        dir = dirs[cur_dir_idx]
        cur_dir_idx = (cur_dir_idx + 1) % len(dirs)
        cur_ele = paths[cur_ele][0 if dir == 'L' else 1]
    return count

def traversePaths(dirs: str, paths: dict[str, list[str]]) -> int:
    start_nodes = [node for node in paths.keys() if node.endswith('A')]
    cycle_lengths = [findCycleLength(node, dirs, paths) for node in start_nodes]
    total_steps = math.lcm(*cycle_lengths)
    return total_steps

dirs, paths = parseInput('../inputs/input8.txt')
print(traversePaths(dirs, paths))