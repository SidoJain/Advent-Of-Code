def parse_input(input_data: str) -> tuple[list[list[str]], str]:
    lines = input_data.strip().split('\n')
    grid = [list(line) for line in lines if len(line) and line[0] == '#']
    moves = ''.join(line for line in lines if len(line) and line[0] not in '#')
    return grid, moves

def find_robot_and_boxes(grid: list[list[str]]) -> tuple[tuple[int, int] | None, set[tuple[int, int]]]:
    robot_pos = None
    box_positions = set()
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == '@':
                robot_pos = (r, c)
            elif cell == 'O':
                box_positions.add((r, c))
    return robot_pos, box_positions

def move_robot(grid: list[list[str]], robot_pos: tuple[int, int], box_positions: set[tuple[int, int]], direction: str) -> tuple[tuple[int, int], set[tuple[int, int]]]:
    dir_map = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    dr, dc = dir_map[direction]
    new_robot_pos = (robot_pos[0] + dr, robot_pos[1] + dc)

    if grid[new_robot_pos[0]][new_robot_pos[1]] == '#':
        return robot_pos, box_positions

    if new_robot_pos in box_positions:
        current_box_pos = new_robot_pos
        box_chain = []

        while current_box_pos in box_positions:
            box_chain.append(current_box_pos)
            current_box_pos = (current_box_pos[0] + dr, current_box_pos[1] + dc)

        if grid[current_box_pos[0]][current_box_pos[1]] == '#' or current_box_pos in box_positions:
            return robot_pos, box_positions

        for box in reversed(box_chain):
            next_box_pos = (box[0] + dr, box[1] + dc)
            box_positions.remove(box)
            box_positions.add(next_box_pos)
        return new_robot_pos, box_positions
    return new_robot_pos, box_positions

def calculate_gps_coordinates(box_positions: set[tuple[int, int]]) -> int:
    return sum(100 * r + c for r, c in box_positions)

def update_grid(grid: list[list[str]], robot_pos: tuple[int, int], box_positions: set[tuple[int, int]]) -> list[list[str]]:
    updated_grid = [row[:] for row in grid]
    for r, row in enumerate(updated_grid):
        for c, _ in enumerate(row):
            if (r, c) == robot_pos:
                updated_grid[r][c] = '@'
            elif (r, c) in box_positions:
                updated_grid[r][c] = 'O'
            elif updated_grid[r][c] not in '#':
                updated_grid[r][c] = '.'
    return updated_grid

def simulate_warehouse(input_data: str) -> int:
    grid, moves = parse_input(input_data)
    robot_pos, box_positions = find_robot_and_boxes(grid)

    for move in moves:
        robot_pos, box_positions = move_robot(grid, robot_pos, box_positions, move)
        grid = update_grid(grid, robot_pos, box_positions)
    return calculate_gps_coordinates(box_positions)

input_data = open('../inputs/input15.txt', 'r').read().strip()
print(simulate_warehouse(input_data))