def readFile(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read().splitlines()

def getPos(data: list[str]) -> tuple[int, int]:
    rowIdx = 0
    colIdx = 0

    for row in data:
        if '^' in row:
            rowIdx = data.index(row)
            colIdx = row.index('^')
            break
        if '<' in row:
            rowIdx = data.index(row)
            colIdx = row.index('<')
            break
        if '>' in row:
            rowIdx = data.index(row)
            colIdx = row.index('>')
            break
        if 'v' in row:
            rowIdx = data.index(row)
            colIdx = row.index('v')
            break

    return (rowIdx, colIdx)

def getNextPos(data: list[str], rowIdx: int, colIdx: int) -> tuple[int, int]:
    row = data[rowIdx]
    if row[colIdx] == '^' and data[rowIdx - 1][colIdx] == '.' and rowIdx != 0:
        data[rowIdx] = data[rowIdx][:colIdx] + '.' + data[rowIdx][colIdx + 1:]
        rowIdx -= 1
        data[rowIdx] = data[rowIdx][:colIdx] + '^' + data[rowIdx][colIdx + 1:]
    elif row[colIdx] == '^' and data[rowIdx - 1][colIdx] == '#' and colIdx != 129:
        data[rowIdx] = data[rowIdx][:colIdx] + '.' + data[rowIdx][colIdx + 1:]
        colIdx += 1
        data[rowIdx] = data[rowIdx][:colIdx] + '>' + data[rowIdx][colIdx + 1:]
    elif rowIdx == 0 or colIdx == 129:
        return (-1, -1)

    if row[colIdx] == '<' and data[rowIdx][colIdx - 1] == '.' and colIdx != 0:
        data[rowIdx] = data[rowIdx][:colIdx] + '.' + data[rowIdx][colIdx + 1:]
        colIdx -= 1
        data[rowIdx] = data[rowIdx][:colIdx] + '<' + data[rowIdx][colIdx + 1:]
    elif row[colIdx] == '<' and data[rowIdx][colIdx - 1] == '#' and rowIdx != 0:
        data[rowIdx] = data[rowIdx][:colIdx] + '.' + data[rowIdx][colIdx + 1:]
        rowIdx -= 1
        data[rowIdx] = data[rowIdx][:colIdx] + '^' + data[rowIdx][colIdx + 1:]
    elif colIdx == 0 or rowIdx == 0:
        return (-1, -1)

    if row[colIdx] == '>' and data[rowIdx][colIdx + 1] == '.' and colIdx != 129:
        data[rowIdx] = data[rowIdx][:colIdx] + '.' + data[rowIdx][colIdx + 1:]
        colIdx += 1
        data[rowIdx] = data[rowIdx][:colIdx] + '>' + data[rowIdx][colIdx + 1:]
    elif row[colIdx] == '>' and data[rowIdx][colIdx + 1] == '#' and rowIdx != 129:
        data[rowIdx] = data[rowIdx][:colIdx] + '.' + data[rowIdx][colIdx + 1:]
        rowIdx += 1
        data[rowIdx] = data[rowIdx][:colIdx] + 'v' + data[rowIdx][colIdx + 1:]
    elif colIdx == 129 or rowIdx == 129:
        return (-1, -1)

    if row[colIdx] == 'v' and data[rowIdx + 1][colIdx] == '.' and rowIdx != 129:
        data[rowIdx] = data[rowIdx][:colIdx] + '.' + data[rowIdx][colIdx + 1:]
        rowIdx += 1
        data[rowIdx] = data[rowIdx][:colIdx] + 'v' + data[rowIdx][colIdx + 1:]
    elif row[colIdx] == 'v' and data[rowIdx + 1][colIdx] == '#' and colIdx != 0:
        data[rowIdx] = data[rowIdx][:colIdx] + '.' + data[rowIdx][colIdx + 1:]
        colIdx -= 1
        data[rowIdx] = data[rowIdx][:colIdx] + '<' + data[rowIdx][colIdx + 1:]
    elif rowIdx == 129 or colIdx == 0:
        return (-1, -1)

    return (rowIdx, colIdx)

def getNumOfSpaces(data: list[str]) -> int:
    visited = set()
    coordinates = getPos(data)
    while True:
        visited.add(coordinates)

        coordinates = getNextPos(data, coordinates[0], coordinates[1])
        if coordinates == (-1, -1):
            break
    return len(visited)

raw_data = readFile('../inputs/input6.txt')
print(getNumOfSpaces(raw_data))