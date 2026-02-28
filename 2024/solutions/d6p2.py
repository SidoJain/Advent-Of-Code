def readFile(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read().splitlines()

def parse_input(map_lines: list[str]) -> tuple[list[list[str]], tuple[int, int], tuple[int, int]]:
    grid = []
    start_pos = None
    start_dir = None
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    for r, line in enumerate(map_lines):
        row = []
        for c, char in enumerate(line):
            if char in directions:
                start_pos = (r, c)
                start_dir = directions[char]
                row.append('.')
            else:
                row.append(char)
        grid.append(row)
    return (grid, start_pos, start_dir)


def simulate(grid: list[list[str]], start_pos: tuple[int, int], start_dir: tuple[int, int], new_obstacle: tuple[int, int]) -> bool:
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_idx = directions.index(start_dir)
    pos = start_pos
    visited_states = set()
    
    if new_obstacle:
        grid[new_obstacle[0]][new_obstacle[1]] = '#'

    while True:
        state = (pos, dir_idx)
        if state in visited_states:
            if new_obstacle:
                grid[new_obstacle[0]][new_obstacle[1]] = '.'
            return True
        visited_states.add(state)

        r, c = pos
        dr, dc = directions[dir_idx]
        next_r, next_c = r + dr, c + dc

        if not (0 <= next_r < rows and 0 <= next_c < cols):
            break
        if grid[next_r][next_c] == '#':
            dir_idx = (dir_idx + 1) % 4
        else:
            pos = (next_r, next_c)

    if new_obstacle:
        grid[new_obstacle[0]][new_obstacle[1]] = '.'
    return False


def getObstructionPosNum(map_lines: list[str]) -> int:
    grid, start_pos, start_dir = parse_input(map_lines)
    rows, cols = len(grid), len(grid[0])
    valid_positions = []

    for r in range(rows):
        for c in range(cols):
            if (r, c) == start_pos or grid[r][c] == '#':
                continue
            if simulate(grid, start_pos, start_dir, (r, c)):
                valid_positions.append((r, c))

    return len(valid_positions)

input_map = readFile('../inputs/input6.txt')
valid_positions = getObstructionPosNum(input_map)
print(valid_positions)