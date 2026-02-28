def readFile(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read().splitlines()

def isXPattern(data: list[str], row: int, col: int) -> bool:
    if (
        data[row][col] in 'MS' and data[row][col + 2] in 'MS' and
        data[row + 1][col + 1] in 'A' and
        data[row + 2][col] in 'MS' and data[row + 2][col] != data[row][col + 2] and data[row + 2][col + 2] in 'MS' and data[row + 2][col + 2] != data[row][col]
    ):
        return True
    return False

def countXPatterns(data: list[str]) -> int:
    count = 0
    num_rows = len(data)
    num_columns = len(data[0]) if data else 0

    for row in range(num_rows - 2):
        for col in range(num_columns - 2):
            if isXPattern(data, row, col):
                count += 1

    return count

raw_data = readFile('../inputs/input4.txt')
count = countXPatterns(raw_data)
print(count)