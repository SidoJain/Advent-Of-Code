def readFile(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read().splitlines()

def getXmax(data: list[str]) -> int:
    count = 0
    num_rows = len(data)
    num_columns = len(data[0])
    diagonals = []

    for offset in range(-(num_rows - 1), num_columns):
        diagonal = ''.join(data[i][i - offset] for i in range(num_rows) if 0 <= i - offset < num_columns)
        diagonals.append(diagonal)

    for offset in range(num_rows + num_columns - 1):
        diagonal = ''.join(data[i][offset - i] for i in range(num_rows) if 0 <= offset - i < num_columns)
        diagonals.append(diagonal)

    for line in data:
        count += line.count('XMAS')
        count += line.count('SAMX')

    for col in range(num_columns):
        column_data = ''.join(row[col] for row in data if col < len(row))
        count += column_data.count('XMAS')
        count += column_data.count('SAMX')

    for diagonal in diagonals:
        count += diagonal.count('XMAS')
        count += diagonal.count('SAMX')

    return count

raw_data = readFile('../inputs/input4.txt')
count = getXmax(raw_data)
print(count)