import re

def parseInput(filename: str) -> list[str]:
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]

def is_symbol(char: str) -> bool:
    return not char.isdigit() and char != '.'

def has_adjacent_symbol(row: int, start_col: int, end_col: int, rows: int, cols: int) -> bool:
    min_row = max(0, row - 1)
    max_row = min(rows - 1, row + 1)
    min_col = max(0, start_col - 1)
    max_col = min(cols - 1, end_col) 

    for r in range(min_row, max_row + 1):
        for c in range(min_col, max_col + 1):
            if is_symbol(lines[r][c]):
                return True
    return False

def sumPartNumbers(lines: list[str]) -> int:
    total_sum = 0
    rows = len(lines)
    cols = len(lines[0])

    for row_idx, line in enumerate(lines):
        for match in re.finditer(r'\d+', line):
            number = int(match.group())
            start_col = match.start()
            end_col = match.end()
            if has_adjacent_symbol(row_idx, start_col, end_col, rows, cols):
                total_sum += number
    return total_sum

lines = parseInput('../inputs/input3.txt')
print(sumPartNumbers(lines))