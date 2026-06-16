from collections import deque

def parseInput(filename: str) -> list[str]:
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]

def countEnclosedTiles(grid: list[str]) -> int:
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
    connects_N = connects_S = connects_E = connects_W = False
    if start_r > 0 and grid[start_r - 1][start_c] in ['|', '7', 'F']:
        s_connections.append((start_r - 1, start_c))
        connects_N = True
    if start_r < rows-1 and grid[start_r + 1][start_c] in ['|', 'L', 'J']:
        s_connections.append((start_r + 1, start_c))
        connects_S = True
    if start_c > 0 and grid[start_r][start_c - 1] in ['-', 'L', 'F']:
        s_connections.append((start_r, start_c - 1))
        connects_W = True
    if start_c < cols-1 and grid[start_r][start_c + 1] in ['-', 'J', '7']:
        s_connections.append((start_r, start_c + 1))
        connects_E = True

    s_pipe = '.'
    if connects_N and connects_S: s_pipe = '|'
    elif connects_E and connects_W: s_pipe = '-'
    elif connects_N and connects_E: s_pipe = 'L'
    elif connects_N and connects_W: s_pipe = 'J'
    elif connects_S and connects_W: s_pipe = '7'
    elif connects_S and connects_E: s_pipe = 'F'

    queue = deque([(start_r, start_c)])
    visited = set([(start_r, start_c)])
    
    for r, c in s_connections:
        queue.append((r, c))
        visited.add((r, c))

    while queue:
        r, c = queue.popleft()
        if grid[r][c] != 'S':
            for dr, dc in pipe_dirs[grid[r][c]]:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

    enclosed_count = 0
    for r in range(rows):
        is_inside = False
        for c in range(cols):
            if (r, c) in visited:
                current_pipe = s_pipe if grid[r][c] == 'S' else grid[r][c]
                if current_pipe in ['|', 'L', 'J']:
                    is_inside = not is_inside
            else:
                if is_inside:
                    enclosed_count += 1
    return enclosed_count

grid = parseInput('../inputs/input10.txt')
print(countEnclosedTiles(grid))