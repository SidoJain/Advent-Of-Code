RED = 12
GREEN = 13
BLUE = 14

def parseInput(filename: str) -> dict[int, str]:
    dictionary = dict()
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            id = int(line.partition(": ")[0].partition(" ")[2])
            games = line.partition(": ")[2]
            dictionary[id] = games
    return dictionary

def isValid(line: str) -> bool:
    valid = True
    games = line.split("; ")
    for game in games:
        cubes = game.split(", ")
        for cube in cubes:
            count = int(cube.split(" ")[0])
            if 'red' in cube and count > RED:
                valid = False
                break
            if 'green' in cube and count > GREEN:
                valid = False
                break
            if 'blue' in cube and count > BLUE:
                valid = False
                break

        if not valid:
            break
    return valid

def countValid(lines: dict[int, str]) -> int:
    count = 0
    for id, games in lines.items():
        if isValid(games):
            count += id
    return count

lines = parseInput('../inputs/input2.txt')
print(countValid(lines))