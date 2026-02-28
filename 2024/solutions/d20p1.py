from collections import defaultdict, deque
import numpy as np

def parse_maze(maze_str: str) -> tuple[np.ndarray, tuple[int, int], tuple[int, int]]:
    lines = maze_str.strip().split('\n')
    maze = np.array([list(line) for line in lines])
    start = tuple(map(lambda x: x[0], np.where(maze == 'S')))
    end = tuple(map(lambda x: x[0], np.where(maze == 'E')))
    maze = (maze != '#').astype(np.uint8)

    return maze, start, end

def calculate_distances(maze: np.ndarray, start_pos: tuple[int, int]) -> np.ndarray:
    height, width = maze.shape
    distances = np.full((height, width), np.inf)
    distances[start_pos] = 0
    queue = deque([start_pos])
    
    while queue:
        r, c = queue.popleft()
        curr_dist = distances[r, c]

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < height and 0 <= nc < width and 
                maze[nr, nc] and distances[nr, nc] == np.inf):
                distances[nr, nc] = curr_dist + 1
                queue.append((nr, nc))
    return distances

def find_cheats(maze: np.ndarray, start_dists: np.ndarray, end_dists: np.ndarray, start_pos: tuple[int, int]) -> dict[int, int]:
    height, width = maze.shape
    normal_time = end_dists[start_pos]
    cheats = defaultdict(int)

    valid_positions = np.where((start_dists != np.inf) & (maze == 1))
    for r, c in zip(*valid_positions):
        time_to_start = start_dists[r, c]
        for dr in range(-2, 3):
            for dc in range(-2, 3):
                nr, nc = r + dr, c + dc
                if not (0 <= nr < height and 0 <= nc < width):
                    continue
                manhattan_dist = abs(dr) + abs(dc)
                if manhattan_dist > 2:
                    continue
                if end_dists[nr, nc] == np.inf:
                    continue

                total_time = time_to_start + manhattan_dist + end_dists[nr, nc]
                time_saved = normal_time - total_time
                if time_saved > 0:
                    cheats[time_saved] += 1
    return cheats

def count_good_cheats(maze_str: str, min_time_saved: int) -> int:
    maze, start_pos, end_pos = parse_maze(maze_str)
    start_dists = calculate_distances(maze, start_pos)
    end_dists = calculate_distances(maze, end_pos)
    cheats = find_cheats(maze, start_dists, end_dists, start_pos)

    return sum(count for time_saved, count in cheats.items() if time_saved >= min_time_saved)

raw_input = open('../inputs/input20.txt').read()
print(count_good_cheats(raw_input, 100))