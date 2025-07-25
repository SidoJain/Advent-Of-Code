def parseInput(grid: list[str]) -> list[tuple[int, int, str]]:
    antennas = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != '.':
                antennas.append((row, col, grid[row][col]))
    return antennas

def getAntinodes(antennas: list[tuple[int, int, str]], width: int, height: int) -> set[tuple[int, int]]:
    antinodes = set()
    freqGroup = {}
    
    for x, y, freq in antennas:
        if freq not in freqGroup:
            freqGroup[freq] = []
        freqGroup[freq].append((x, y))

    for freq, positions in freqGroup.items():
        n = len(positions)
        for i in range(n - 1):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                dx = x2 - x1
                dy = y2 - y1
                antinode1 = (x1 - dx, y1 - dy)
                antinode2 = (x2 + dx, y2 + dy)

                while 0 <= antinode1[0] < width and 0 <= antinode1[1] < height:
                    antinodes.add(antinode1)
                    antinode1 = (antinode1[0] - dx, antinode1[1] - dy)

                while 0 <= antinode2[0] < width and 0 <= antinode2[1] < height:
                    antinodes.add(antinode2)
                    antinode2 = (antinode2[0] + dx, antinode2[1] + dy)

    return antinodes

def checkCollinear(A: tuple[int, int], B: tuple[int, int], C: tuple[int, int]) -> bool:
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    return (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)

def checkInline(antennas: list[tuple[int, int, str]], antinodes: list[tuple[int, int]]) -> list[tuple[int, int]]:
    for antenna in antennas:
        for i in range(len(antinodes) - 1):
            flag = True
            for j in range(i + 1, len(antinodes)):
                if checkCollinear((antenna[0], antenna[1]), antinodes[i], antinodes[j]):
                    antinodes.append((antenna[0], antenna[1]))
                    flag = False
                    break
            if not flag:
                break
    return antinodes

def countAntinodes(grid: list[str]) -> int:
    height, width = len(grid), len(grid[0])
    antennas = parseInput(grid)
    antinodes = getAntinodes(antennas, width, height)    
    antinodes = set(checkInline(antennas, list(antinodes)))
    return len(antinodes)

grid = open('../inputs/input8.txt').read().splitlines()
print(countAntinodes(grid))