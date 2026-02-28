def count_accessible(grid: list[str]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    ans = 0
    dirs = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)]
    for row in range(rows):
        for col in range(cols):
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
                ans += 1
    return ans

with open("../inputs/input4.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
print(count_accessible(lines))