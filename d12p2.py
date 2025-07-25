def neighbours(x: int, y: int) -> set[tuple[int, int]]:
    return {(x + dx, y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]}
    
def neighbours_in_same_region(x: int, y: int) -> set[tuple[int, int]]:
    return {(x1, y1) for x1, y1 in neighbours(x, y)
            if 0 <= x1 < rows and 0 <= y1 < cols and grid[x][y] == grid[x1][y1]}

def count_corners(x: int, y: int, region: set[tuple[int, int]]) -> int:
    return sum(((x, y + dy) not in region and (x + dx, y) not in region) or 
                ((x, y + dy) in region and (x + dx, y) in region and (x + dx, y + dy) not in region)
                for dx in (1, -1) for dy in (1, -1))

grid = open('../inputs/input12.txt').read().splitlines()
rows, cols = len(grid), len(grid[0])

result = 0
remaining_plots = {(x,y) for x in range(rows) for y in range(cols)} 

while remaining_plots:
    region = set()
    frontier = {remaining_plots.pop()}
    while frontier:
        region.add(plot := frontier.pop())
        new_frontier = neighbours_in_same_region(*plot) & remaining_plots
        frontier |= new_frontier
        remaining_plots -= new_frontier
    result += len(region) * sum(count_corners(plot[0], plot[1], region) for plot in region)

print(result)