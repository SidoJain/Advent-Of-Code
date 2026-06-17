def parseInput(filename: str) -> tuple[str, ...]:
    with open(filename) as file:
        return tuple(line.strip() for line in file.readlines())

def transpose(matrix: tuple[str, ...]) -> tuple[str, ...]:
    return tuple("".join(col) for col in zip(*matrix))

def moveLeft(row_str: str) -> str:
    parts = row_str.split('#')
    return '#'.join('O' * p.count('O') + '.' * p.count('.') for p in parts)

def moveRight(row_str: str) -> str:
    parts = row_str.split('#')
    return '#'.join('.' * p.count('.') + 'O' * p.count('O') for p in parts)

def spinCycle(grid: tuple[str, ...]) -> tuple[str, ...]:
    grid = transpose(grid)
    grid = tuple(moveLeft(row) for row in grid)
    grid = transpose(grid)
    grid = tuple(moveLeft(row) for row in grid)
    grid = transpose(grid)
    grid = tuple(moveRight(row) for row in grid)
    grid = transpose(grid)
    grid = tuple(moveRight(row) for row in grid)

    return grid

def calcTotalLoad(grid: tuple[str, ...]) -> int:
    seen_states = {}
    history = []
    target_cycles = 1000000000
    for i in range(target_cycles):
        if grid in seen_states:
            cycle_start = seen_states[grid]
            cycle_length = i - cycle_start
            remaining_cycles = target_cycles - i
            final_index = cycle_start + (remaining_cycles % cycle_length)
            grid = history[final_index]
            break

        seen_states[grid] = i
        history.append(grid)
        grid = spinCycle(grid)

    total_load = 0
    num_rows = len(grid)
    for i, row in enumerate(grid):
        weight = num_rows - i
        total_load += row.count('O') * weight
    return total_load

grid = parseInput('../inputs/input14.txt')
print(calcTotalLoad(grid))