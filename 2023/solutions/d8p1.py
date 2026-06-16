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

def traversePath(dirs: str, paths: dict[str, list[str]]) -> int:
    count = 0
    cur_dir_idx = 0
    cur_ele = 'AAA'
    while cur_ele != 'ZZZ':
        count += 1
        dir = dirs[cur_dir_idx]
        cur_dir_idx = (cur_dir_idx + 1) % len(dirs)
        cur_ele = paths[cur_ele][0 if dir == 'L' else 1]
    return count

dirs, paths = parseInput('../inputs/input8.txt')
print(traversePath(dirs, paths))