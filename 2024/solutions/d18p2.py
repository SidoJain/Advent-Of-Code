from collections import deque
from collections.abc import Iterator

def parse_input(input_str: str) -> list[tuple[int, int]]:
    return [tuple(map(int, line.split(','))) for line in input_str.strip().splitlines()]

def simulate_falling_bytes(grid_size: int, byte_positions: list[tuple[int, int]]) -> Iterator[tuple[list[list[bool]], tuple[int, int], int]]:
    grid = [[False for _ in range(grid_size)] for _ in range(grid_size)]
    for step, (x, y) in enumerate(byte_positions, start=1):
        grid[y][x] = True
        yield grid, (x, y), step

def is_path_blocked(grid: list[list[bool]], start: tuple[int, int], goal: tuple[int, int]) -> bool:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([start])
    visited = set()
    visited.add(start)
    
    while queue:
        x, y = queue.popleft()
        if (x, y) == goal:
            return False
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid) and not grid[ny][nx] and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    return True

example_input = open('../inputs/input18.txt').read()
byte_positions = parse_input(example_input)
grid_size = 71
start = (0, 0)
goal = (70, 70)

for grid, (x, y), step in simulate_falling_bytes(grid_size, byte_positions):
    if is_path_blocked(grid, start, goal):
        print(f'{x},{y}')
        break