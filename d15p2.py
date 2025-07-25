def try_push(grid: list[list[str]], pos_x: int, pos_y: int, dx: int, dy: int) -> bool:
    new_x = pos_x + dx
    new_y = pos_y + dy

    if grid[new_x][new_y] == '#':
        return False
    elif grid[new_x][new_y] == '.':
        return True

    if dy == 0:
        if grid[new_x][new_y] == ']':
            return try_push(grid, new_x, new_y, dx, dy) and try_push(grid, new_x, new_y-1, dx, dy)
        elif grid[new_x][new_y] == '[':
            return try_push(grid, new_x, new_y, dx, dy) and try_push(grid, new_x, new_y+1, dx, dy)
    elif dy == -1 and grid[new_x][new_y] == ']':
        return try_push(grid, new_x, new_y-1, dx, dy)
    elif dy == 1 and grid[new_x][new_y] == '[':
        return try_push(grid, new_x, new_y+1, dx, dy)

    return False

def push(grid: list[list[str]], pos_x: int, pos_y: int, dx: int, dy: int) -> None:
    new_x = pos_x + dx
    new_y = pos_y + dy

    if grid[new_x][new_y] == '#':
        return
    elif grid[new_x][new_y] == '.':
        grid[pos_x][pos_y], grid[new_x][new_y] = grid[new_x][new_y], grid[pos_x][pos_y]
        return

    if dy == 0:
        if grid[new_x][new_y] == ']':
            push(grid, new_x, new_y, dx, dy)
            push(grid, new_x, new_y - 1, dx, dy)
            grid[pos_x][pos_y], grid[new_x][new_y] = grid[new_x][new_y], grid[pos_x][pos_y]
        elif grid[new_x][new_y] == '[':
            push(grid, new_x, new_y, dx, dy)
            push(grid, new_x, new_y + 1, dx, dy)
            grid[pos_x][pos_y], grid[new_x][new_y] = grid[new_x][new_y], grid[pos_x][pos_y]
    elif dy == -1 and grid[new_x][new_y] == ']':
        push(grid, new_x, new_y - 1, dx, dy)
        grid[new_x][new_y - 1], grid[new_x][new_y], grid[pos_x][pos_y] = grid[new_x][new_y], grid[pos_x][pos_y], grid[new_x][new_y - 1]
    elif dy == 1 and grid[new_x][new_y] == '[':
        push(grid, new_x, new_y + 1, dx, dy)
        grid[new_x][new_y + 1], grid[new_x][new_y], grid[pos_x][pos_y] = grid[new_x][new_y], grid[pos_x][pos_y], grid[new_x][new_y + 1]

def simulate_warehouse(raw_data: list[str]) -> int:
    small_grid = raw_data[0].split('\n')
    moves = ''.join(raw_data[1].split('\n'))
    rows = len(small_grid)
    cols = len(small_grid[0]) * 2
    for i in range(rows):
        row = []
        for col in small_grid[i]:
            if col == '#':
                row.append('#')
                row.append('#')
            elif col == 'O':
                row.append('[')
                row.append(']')
            elif col == '.':
                row.append('.')
                row.append('.')
            else:
                row.append('@')
                row.append('.')

        small_grid[i] = row
        for j in range(cols):
            if small_grid[i][j] == '@':
                sx = i
                sy = j
                small_grid[i][j] = '.'

    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    for move in moves:
        if move == '<':
            dir = 0
        elif move == '^':
            dir = 1
        elif move == '>':
            dir = 2
        else:
            dir = 3
        if try_push(small_grid, sx, sy, dx[dir], dy[dir]):
            push(small_grid, sx, sy, dx[dir], dy[dir])
            sx += dx[dir]
            sy += dy[dir]

    result = 0
    for i in range(rows):
        for j in range(cols):
            if small_grid[i][j] == '[':
                result += 100 * i + j
    return result

raw_data = open('../inputs/input15.txt').read().strip().split('\n\n')
print(simulate_warehouse(raw_data))