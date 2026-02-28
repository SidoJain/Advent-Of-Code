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

def find_lowest_paths(grid: list[str], start: tuple[int, int], end: tuple[int, int]) -> tuple[int, list[list[tuple[int, int]]]]:
    start_state = (0, start, 'E', [start])
    pq = [start_state]
    visited = {}
    lowest_score = float('inf')
    paths_with_lowest_score = []

    while pq:
        score, position, direction, path = heappop(pq)
        if (position, direction) in visited and score > visited[(position, direction)][0]:
            continue
        visited[(position, direction)] = (score, path)

        if position == end:
            if score < lowest_score:
                lowest_score = score
                paths_with_lowest_score = [path]
            elif score == lowest_score:
                paths_with_lowest_score.append(path)

        for neighbor, new_dir, cost in get_neighbors(position, direction, grid):
            new_score = score + cost
            new_path = path + [neighbor]
            heappush(pq, (new_score, neighbor, new_dir, new_path))
    return int(lowest_score), paths_with_lowest_score

def count_unique_tiles(paths: list[list[tuple[int, int]]]) -> int:
    unique_tiles = set()
    for path in paths:
        unique_tiles.update(path)
    return len(unique_tiles)

maze_input = open('../inputs/input16.txt').read()
grid, start, end = parse_input(maze_input)
lowest_score, paths_with_lowest_score = find_lowest_paths(grid, start, end)
unique_tile_count = count_unique_tiles(paths_with_lowest_score)
print('Lowest score:', lowest_score)
print('Number of unique tiles in minimum-cost paths:', unique_tile_count)