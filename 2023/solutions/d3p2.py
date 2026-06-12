import re
from collections import defaultdict

def parseInput(filename: str) -> list[str]:
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]

def find_adjacent_stars(row: int, start_col: int, end_col: int, rows: int, cols: int) -> set:
    min_row = max(0, row - 1)
    max_row = min(rows - 1, row + 1)
    min_col = max(0, start_col - 1)
    max_col = min(cols - 1, end_col) 
    adjacent_star_coords = set()

    for r in range(min_row, max_row + 1):
        for c in range(min_col, max_col + 1):
            if lines[r][c] == '*':
                adjacent_star_coords.add((r, c))
    return adjacent_star_coords

def sumGearRatios(lines: list[str]) -> int:
    rows = len(lines)
    cols = len(lines[0])
    stars = defaultdict(list)

    for row_idx, line in enumerate(lines):
        for match in re.finditer(r'\d+', line):
            number = int(match.group())
            start_col = match.start()
            end_col = match.end()

            adj_stars = find_adjacent_stars(row_idx, start_col, end_col, rows, cols)
            for star_pos in adj_stars:
                stars[star_pos].append(number)

    total_gear_ratio = 0
    for star_pos, attached_numbers in stars.items():
        if len(attached_numbers) == 2:
            gear_ratio = attached_numbers[0] * attached_numbers[1]
            total_gear_ratio += gear_ratio
    return total_gear_ratio

lines = parseInput('../inputs/input3.txt')
print(sumGearRatios(lines))