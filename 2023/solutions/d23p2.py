def parseInput(filename: str) -> list[list[str]]:
    with open(filename) as file:
        return [list(line.strip()) for line in file if line.strip()]

def calcLongestDryHike(grid: list[list[str]]) -> int:
    ROWS = len(grid)
    COLS = len(grid[0])

    start = (0, grid[0].index('.'))
    end = (ROWS - 1, grid[ROWS - 1].index('.'))
    nodes = [start, end]
    for r in range(1, ROWS - 1):
        for c in range(1, COLS - 1):
            if grid[r][c] == '#':
                continue

            neighbors = 0
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if grid[r + dr][c + dc] != '#':
                    neighbors += 1
            if neighbors > 2:
                nodes.append((r, c))

    graph = {n: {} for n in nodes}
    for node in nodes:
        stack = [(node[0], node[1], 0)]
        visited = {node}
        while stack:
            r, c, dist = stack.pop()
            if dist != 0 and (r, c) in nodes:
                graph[node][(r, c)] = dist
                continue

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != '#':
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        stack.append((nr, nc, dist + 1))

    visited = set()
    max_dist = 0

    def dfs(curr_node, current_dist):
        nonlocal max_dist
        if curr_node == end:
            max_dist = max(max_dist, current_dist)
            return

        visited.add(curr_node)
        for nxt_node, edge_weight in graph[curr_node].items():
            if nxt_node not in visited:
                dfs(nxt_node, current_dist + edge_weight)
        visited.remove(curr_node)

    dfs(start, 0)
    return max_dist

grid = parseInput('../inputs/input23.txt')
print(calcLongestDryHike(grid))