def count_accessible_fast(grid: list[list[str]], active: set[tuple[int, int]], rows: int, cols: int, dirs: list[tuple[int, int]]) -> list[tuple[int, int]]:
    to_remove = []
    for row, col in active:
        if grid[row][col] != '@':
            continue
        count = 0
        for dr, dc in dirs:
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                count += 1
                if count == 4:
                    break
        if count < 4:
            to_remove.append((row, col))
    return to_remove

with open("../inputs/input4.txt", "r") as file:
    lines = [list(line.strip()) for line in file.readlines()]

rows = len(lines)
cols = len(lines[0])
dirs = [(-1,-1),(-1,0),(-1,1),
        (0,-1),         (0,1),
        (1,-1),(1,0),(1,1)]

active = {(row, col) for row in range(rows) for col in range(cols) if lines[row][col] == '@'}
total_removed = 0
while True:
    accessible = count_accessible_fast(lines, active, rows, cols, dirs)
    if not accessible:
        break

    total_removed += len(accessible)
    next_active = set()
    for row, col in accessible:
        lines[row][col] = '.'
        for dr, dc in dirs + [(0,0)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                next_active.add((nr, nc))
    active = next_active
print(total_removed)