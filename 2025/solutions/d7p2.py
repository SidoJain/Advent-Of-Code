def count_timelines(manifold: list[str]) -> int:
    rows, cols = len(manifold), len(manifold[0])
    start_r, start_c = next((row, col) for row in range(rows) for col in range(cols) if manifold[row][col] == 'S')

    dp_next = [1] * cols
    for row in range(rows - 1, start_r, -1):
        dp_cur = [0] * cols
        for col in range(cols):
            if manifold[row][col] == '.':
                dp_cur[col] = dp_next[col]

        for col in range(cols):
            if manifold[row][col] == '^':
                left = dp_cur[col - 1] if col - 1 >= 0 else 0
                right = dp_cur[col + 1] if col + 1 < cols else 0
                dp_cur[col] = left + right
        dp_next = dp_cur
    return dp_next[start_c]

with open("../inputs/input7.txt", "r") as file:
    manifold = [line.strip() for line in file.readlines()]
print(count_timelines(manifold))