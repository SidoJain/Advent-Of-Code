import heapq

def parseInput(filename: str) -> list[list[int]]:
    with open(filename) as file:
        return [[int(char) for char in line.strip()] for line in file if line.strip()]

def calcMinHeatLoss(grid: list[list[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    pq = [(0, 0, 0, 0, 0, 0)]
    seen = set()
    while pq:
        heat, r, c, dr, dc, steps = heapq.heappop(pq)
        if r == rows - 1 and c == cols - 1:
            return heat

        state = (r, c, dr, dc, steps)
        if state in seen:
            continue

        seen.add(state)
        for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (ndr, ndc) == (-dr, -dc) and (dr, dc) != (0, 0):
                continue
            if (ndr, ndc) == (dr, dc):
                n_steps = steps + 1
            else:
                n_steps = 1
            if n_steps > 3:
                continue

            nr, nc = r + ndr, c + ndc
            if 0 <= nr < rows and 0 <= nc < cols:
                n_heat = heat + grid[nr][nc]
                heapq.heappush(pq, (n_heat, nr, nc, ndr, ndc, n_steps))
    return -1

grid = parseInput('../inputs/input17.txt')
print(calcMinHeatLoss(grid))