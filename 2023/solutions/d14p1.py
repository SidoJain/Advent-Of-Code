def parseInput(filename: str) -> list[str]:
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]

def transpose(matrix: list[str]) -> list[list[str]]:
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def moveCircleRocksLeft(row: list[str]) -> list[str]:
    row_str = "".join(row)
    parts = row_str.split('#')
    new_parts = []
    for part in parts:
        o_count = part.count('O')
        dot_count = part.count('.')
        new_parts.append('O' * o_count + '.' * dot_count)

    new_row_str = '#'.join(new_parts)
    return list(new_row_str)

def calcTotalLoad(grid: list[str]) -> int:
    transposed_grid = transpose(grid)
    tilted_transposed = [moveCircleRocksLeft(row) for row in transposed_grid]
    tilted_grid_strings = ["".join(row) for row in tilted_transposed]
    final_grid = transpose(tilted_grid_strings)

    total_load = 0
    num_rows = len(final_grid)
    for i, row in enumerate(final_grid):
        weight = num_rows - i
        o_count = row.count('O')
        total_load += o_count * weight
    return total_load

grid = parseInput('../inputs/input14.txt')
print(calcTotalLoad(grid))