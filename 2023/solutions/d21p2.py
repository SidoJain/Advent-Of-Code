def parseInput(filename: str) -> list[list[str]]:
    with open(filename) as file:
        return [list(line.strip()) for line in file if line.strip()]

def calcInfiniteElfPositions(grid: list[list[str]], target_steps: int) -> int:
    size = len(grid)
    start_pos = None
    for r in range(size):
        for c in range(size):
            if grid[r][c] == 'S':
                start_pos = (r, c)
                break
        if start_pos:
            break

    current_positions = {start_pos}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    remainder = target_steps % size
    points = []
    step_count = 0
    while len(points) < 3:
        if step_count == remainder or step_count == remainder + size or step_count == remainder + 2 * size:
            points.append(len(current_positions))
        
        next_positions = set()
        for r, c in current_positions:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if grid[nr % size][nc % size] != '#':
                    next_positions.add((nr, nc))
        current_positions = next_positions
        step_count += 1

    y0, y1, y2 = points
    n = target_steps // size
    a = (y2 - 2 * y1 + y0) // 2
    b = y1 - y0 - a
    c = y0
    return a * n ** 2 + b * n + c

grid = parseInput('../inputs/input21.txt')
print(calcInfiniteElfPositions(grid, target_steps=26501365))