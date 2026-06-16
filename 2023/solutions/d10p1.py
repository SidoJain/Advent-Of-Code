from collections import deque

def parseInput(filename: str) -> list[str]:
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]

def findFarthestPipe(grid: list[str]) -> int:
    rows, cols = len(grid), len(grid[0])
    N, S, E, W = (-1, 0), (1, 0), (0, 1), (0, -1)
    pipe_dirs = {
        '|': [N, S],
        '-': [E, W],
        'L': [N, E],
        'J': [N, W],
        '7': [S, W],
        'F': [S, E],
        '.': []
    }

    start_r, start_c = -1, -1
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start_r, start_c = r, c
                break
        if start_r != -1: break

    s_connections = []
    if start_r > 0 and grid[start_r - 1][start_c] in ['|', '7', 'F']:
        s_connections.append((start_r - 1, start_c))
    if start_r < rows-1 and grid[start_r + 1][start_c] in ['|', 'L', 'J']:
        s_connections.append((start_r + 1, start_c))
    if start_c > 0 and grid[start_r][start_c - 1] in ['-', 'L', 'F']:
        s_connections.append((start_r, start_c - 1))
    if start_c < cols-1 and grid[start_r][start_c + 1] in ['-', 'J', '7']:
        s_connections.append((start_r, start_c + 1))

    queue = deque([(start_r, start_c, 0)])
    visited = set([(start_r, start_c)])
    max_distance = 0
    for r, c in s_connections:
        queue.append((r, c, 1))
        visited.add((r, c))

    while queue:
        r, c, dist = queue.popleft()
        max_distance = max(max_distance, dist)
        if grid[r][c] != 'S':
            for dr, dc in pipe_dirs[grid[r][c]]:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))
    return max_distance

grid = parseInput('../inputs/input10.txt')
print(findFarthestPipe(grid))