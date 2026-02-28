def parseInput(grid: list[str]) -> list[tuple[int, int, str]]:
    antennas = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != '.':
                antennas.append((row, col, grid[row][col]))
    return antennas

def getAntinodes(antennas: list[tuple[int, int, str]], width: int, height: int) -> set[tuple[int, int]]:
    antinodes = set()
    freqGroups = {}
    
    for x, y, freq in antennas:
        if freq not in freqGroups:
            freqGroups[freq] = []
        freqGroups[freq].append((x, y))

    for freq, positions in freqGroups.items():
        n = len(positions)
        for i in range(n - 1):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                dx = x2 - x1
                dy = y2 - y1
                antinode1 = (x1 - dx, y1 - dy)
                antinode2 = (x2 + dx, y2 + dy)

                if 0 <= antinode1[0] < width and 0 <= antinode1[1] < height:
                    antinodes.add(antinode1)
                if 0 <= antinode2[0] < width and 0 <= antinode2[1] < height:
                    antinodes.add(antinode2)

    return antinodes

def countAntinodes(grid: list[str]) -> int:
    height, width = len(grid), len(grid[0])
    antennas = parseInput(grid)
    antinodes = getAntinodes(antennas, width, height)
    return len(antinodes)

grid = open('../inputs/input8.txt').read().splitlines()
print(countAntinodes(grid))