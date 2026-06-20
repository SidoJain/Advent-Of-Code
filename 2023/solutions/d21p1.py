def parseInput(filename: str) -> list[list[str]]:
    with open(filename) as file:
        return [list(line.strip()) for line in file if line.strip()]

def getElfPositions(grid: list[list[str]], steps: int) -> int:
    rows = len(grid)
    cols = len(grid[0])

    start_pos = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start_pos = (r, c)
                break
        if start_pos:
            break

    current_positions = {start_pos}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for _ in range(steps):
        next_positions = set()
        for r, c in current_positions:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                    next_positions.add((nr, nc))
        current_positions = next_positions
    return len(current_positions)

grid = parseInput('../inputs/input21.txt')
print(getElfPositions(grid, steps=64))