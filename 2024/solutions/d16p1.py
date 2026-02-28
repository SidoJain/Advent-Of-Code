from heapq import heappush, heappop

def parse_input(input_string: str) -> tuple[list[str], tuple[int, int], tuple[int, int]]:
    grid = input_string.strip().split('\n')
    start, end = None, None
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == 'S':
                start = (r, c)
            elif char == 'E':
                end = (r, c)
    return grid, start, end

def get_neighbors(position: tuple[int, int], direction: str, grid: list[str]) -> list[tuple[tuple[int, int], str, int]]:
    directions = ['N', 'E', 'S', 'W']
    deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    x, y = position
    dir_idx = directions.index(direction)
    
    neighbors = []
    dx, dy = deltas[dir_idx]
    if grid[x + dx][y + dy] != '#':
        neighbors.append(((x + dx, y + dy), direction, 1))
    neighbors.append((position, directions[(dir_idx + 1) % 4], 1000))
    neighbors.append((position, directions[(dir_idx - 1) % 4], 1000))

    return neighbors

def find_lowest_score(grid: list[str], start: tuple[int, int], end: tuple[int, int]) -> int:
    start_state = (0, start, 'E')
    pq = [start_state]
    visited = set()
    
    while pq:
        score, position, direction = heappop(pq)
        if (position, direction) in visited:
            continue
        visited.add((position, direction))
        
        if position == end:
            return score
        
        for neighbor, new_dir, cost in get_neighbors(position, direction, grid):
            if (neighbor, new_dir) not in visited:
                new_score = score + cost
                heappush(pq, (new_score, neighbor, new_dir))
    return -1

maze_input = open('../inputs/input16.txt').read()
grid, start, end = parse_input(maze_input)
lowest_score = find_lowest_score(grid, start, end)
print('Lowest score:', lowest_score)