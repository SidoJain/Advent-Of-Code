import itertools

def parseInput(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def calcGalaxyDistances(grid: list[str], expansion_factor: int) -> int:
    rows = len(grid)
    cols = len(grid[0])

    empty_rows = [r for r in range(rows) if all(char == '.' for char in grid[r])]
    empty_cols = [c for c in range(cols) if all(grid[r][c] == '.' for r in range(rows))]

    galaxies = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '#':
                galaxies.append((r, c))

    total_distance = 0
    extra_steps = expansion_factor - 1
    for (r1, c1), (r2, c2) in itertools.combinations(galaxies, 2):
        dist = abs(r1 - r2) + abs(c1 - c2)
        min_r, max_r = min(r1, r2), max(r1, r2)
        for er in empty_rows:
            if min_r < er < max_r:
                dist += extra_steps 

        min_c, max_c = min(c1, c2), max(c1, c2)
        for ec in empty_cols:
            if min_c < ec < max_c:
                dist += extra_steps
        total_distance += dist
    return total_distance

grid = parseInput('../inputs/input11.txt')
print(calcGalaxyDistances(grid, 1000000))