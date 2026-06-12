def parseInput(filename: str) -> list[str]:
    parsed_lines = []
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            parsed_lines.append(line.partition(": ")[2])
    return parsed_lines

def countPower(line: str) -> int:
    min_red = 0
    min_green = 0
    min_blue = 0

    games = line.split('; ')
    for game in games:
        cubes = game.split(', ')
        for cube in cubes:
            count = int(cube.split(' ')[0])
            if 'red' in cube and min_red < count:
                min_red = count
            if 'green' in cube and min_green < count:
                min_green = count
            if 'blue' in cube and min_blue < count:
                min_blue = count
    return min_red * min_green * min_blue

def countPowers(lines: list[str]) -> int:
    powers = 0
    for line in lines:
        powers += countPower(line)
    return powers

lines = parseInput('../inputs/input2.txt')
print(countPowers(lines))