from collections import deque

def parse_map(input_map: list[str]) -> list[list[int]]:
    return [list(map(int, line.strip())) for line in input_map]

def get_neighbors(x: int, y: int, height: int, grid: list[list[int]]) -> list[tuple[int, int]]:
    neighbors = []
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == height + 1:
            neighbors.append((nx, ny))
    return neighbors

def count_score(trailhead: tuple[int, int], grid: list[list[int]]) -> int:
    visited = set()
    queue = deque([trailhead])
    reachable_nines = set()

    while queue:
        x, y = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if grid[x][y] == 9:
            reachable_nines.add((x, y))
        for neighbor in get_neighbors(x, y, grid[x][y], grid):
            queue.append(neighbor)
    return len(reachable_nines)

def count_total_score(input_map: list[str]) -> int:
    grid = parse_map(input_map)
    rows, cols = len(grid), len(grid[0])
    total_score = 0
    trailheads = [(x, y) for x in range(rows) for y in range(cols) if grid[x][y] == 0]

    for trailhead in trailheads:
        total_score += count_score(trailhead, grid)
    return total_score

input_map = open('../inputs/input10.txt').read().strip().split('\n')
print(count_total_score(input_map))