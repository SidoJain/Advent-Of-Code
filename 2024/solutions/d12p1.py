from collections import deque

def parse_map(input_map: list[str]) -> list[list[str]]:
    return [list(row) for row in input_map]

def flood_fill(grid: list[list[str]], x: int, y: int, visited: set[tuple[int, int]]) -> tuple[int, int]:
    region_type = grid[x][y]
    area = 0
    perimeter = 0
    rows, cols = len(grid), len(grid[0])
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(x, y)])
    visited.add((x, y))

    while queue:
        cx, cy = queue.popleft()
        area += 1
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == region_type:
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                else:
                    perimeter += 1
            else:
                perimeter += 1
    return area, perimeter

def calculate_total_price(input_map: list[str]) -> int:
    grid = parse_map(input_map)
    visited = set()
    total_price = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x, y) not in visited:
                area, perimeter = flood_fill(grid, x, y, visited)
                total_price += area * perimeter
    return total_price

raw_data = open('../inputs/input12.txt').read().splitlines()
total_price = calculate_total_price(raw_data)
print(total_price)