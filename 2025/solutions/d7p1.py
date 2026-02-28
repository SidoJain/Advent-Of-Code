def count_beam_splits(manifold: list[str]) -> int:
    rows, cols = len(manifold), len(manifold[0])
    start_r, start_c = next((row, col) for row in range(rows) for col in range(cols) if manifold[row][col] == 'S')

    visited = set()
    stack = [(start_r, start_c)] 
    split_count = 0
    while stack:
        row, col = stack.pop()
        key = (row, col)
        if key in visited:
            continue
        visited.add(key)

        dr, dc = (1, 0)
        nr, nc = row + dr, col + dc
        if not (0 <= nr < rows and 0 <= nc < cols):
            continue

        cell = manifold[nr][nc]
        if cell == '.':
            stack.append((nr, nc))
        elif cell == '^':
            split_count += 1
            for dc_offset in [-1, 1]:
                sr, sc = nr, nc + dc_offset
                if 0 <= sc < cols and manifold[sr][sc] != '#':
                    stack.append((sr, sc))
    return split_count

with open("../inputs/input7.txt", "r") as file:
    manifold = [line.strip() for line in file.readlines()]
print(count_beam_splits(manifold))