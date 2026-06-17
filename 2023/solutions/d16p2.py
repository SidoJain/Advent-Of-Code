from collections import deque

def parseInput(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def countEnergizedTiles(grid: list[str], start_state: tuple[int, int, int, int]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    queue = deque([start_state])
    seen_states = set()
    energized_positions = set()
    while queue:
        r, c, dr, dc = queue.popleft()
        if r < 0 or r >= rows or c < 0 or c >= cols:
            continue

        state = (r, c, dr, dc)
        if state in seen_states:
            continue

        seen_states.add(state)
        energized_positions.add((r, c))
        char = grid[r][c]
        match char:
            case '.':
                queue.append((r + dr, c + dc, dr, dc))
            case '/':
                ndr, ndc = -dc, -dr
                queue.append((r + ndr, c + ndc, ndr, ndc))
            case '\\':
                ndr, ndc = dc, dr
                queue.append((r + ndr, c + ndc, ndr, ndc))
            case '|':
                if dc != 0:
                    queue.append((r - 1, c, -1, 0))
                    queue.append((r + 1, c, 1, 0))
                else:
                    queue.append((r + dr, c + dc, dr, dc))
            case '-':
                if dr != 0:
                    queue.append((r, c - 1, 0, -1))
                    queue.append((r, c + 1, 0, 1))
                else:
                    queue.append((r + dr, c + dc, dr, dc))
    return len(energized_positions)

def countTotalEnergizedTiles(grid: list[str]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    max_energized = 0

    for c in range(cols):
        max_energized = max(max_energized, countEnergizedTiles(grid, (0, c, 1, 0)))
        max_energized = max(max_energized, countEnergizedTiles(grid, (rows - 1, c, -1, 0)))
    for r in range(rows):
        max_energized = max(max_energized, countEnergizedTiles(grid, (r, 0, 0, 1)))
        max_energized = max(max_energized, countEnergizedTiles(grid, (r, cols - 1, 0, -1)))
    return max_energized

grid = parseInput('../inputs/input16.txt')
print(countTotalEnergizedTiles(grid))