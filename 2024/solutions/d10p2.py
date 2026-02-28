def parse_map(input_map: list[str]) -> list[list[int]]:
    return [list(map(int, line.strip())) for line in input_map]

def count_valid_trails(x: int, y: int, grid: list[list[int]], visited: set[tuple[int, int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    if grid[x][y] == 9:
        return 1

    visited.add((x, y))
    total_trails = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if (0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] == grid[x][y] + 1):
            total_trails += count_valid_trails(nx, ny, grid, visited)

    visited.remove((x, y))
    return total_trails

def count_ratings(input_map: list[str]) -> int:
    grid = parse_map(input_map)
    rows, cols = len(grid), len(grid[0])
    total_rating = 0
    trailheads = [(x, y) for x in range(rows) for y in range(cols) if grid[x][y] == 0]

    for trailhead in trailheads:
        visited = set()
        x, y = trailhead
        rating = count_valid_trails(x, y, grid, visited)
        total_rating += rating
    return total_rating

input_map = open('../inputs/input10.txt').read().strip().split('\n')
print(count_ratings(input_map))