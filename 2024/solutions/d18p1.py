from collections import deque

def parse_input(input_str: str) -> list[tuple[int, int]]:
    return [tuple(map(int, line.split(','))) for line in input_str.strip().splitlines()]

def simulate_falling_bytes(grid_size: int, byte_positions: list[tuple[int, int]], num_bytes: int) -> list[list[bool]]:
    grid = [[False for _ in range(grid_size)] for _ in range(grid_size)]
    for x, y in byte_positions[:num_bytes]:
        grid[y][x] = True
    return grid

def shortest_path(grid: list[list[bool]], start: tuple[int, int], goal: tuple[int, int]) -> int:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)
    
    while queue:
        (x, y), steps = queue.popleft()
        if (x, y) == goal:
            return steps
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid) and not grid[ny][nx] and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))
    return -1

example_input = open('../inputs/input18.txt').read()
byte_positions = parse_input(example_input)
grid_size = 71
num_bytes = 1024
grid = simulate_falling_bytes(grid_size, byte_positions, num_bytes)
start = (0, 0)
goal = (70, 70)

shortest_steps = shortest_path(grid, start, goal)
print(f'Shortest steps: {shortest_steps}')