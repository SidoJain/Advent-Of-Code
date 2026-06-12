def parseInput(filename: str) -> list[str]:
    with open(filename) as file:
        return [line.strip().split(': ')[1] for line in file.readlines()]

def countPoint(line: str) -> int:
    winning, ours = line.split(' | ')
    winning_set = {int(num) for num in winning.split()}
    ours = [int(num) for num in ours.split()]

    point = 0
    for num in ours:
        if num in winning_set:
            if not point:
                point = 1
            else:
                point *= 2
    return point

def countPoints(lines: list[str]) -> int:
    count = 0
    for line in lines:
        count += countPoint(line)
    return count

lines = parseInput('../inputs/input4.txt')
print(countPoints(lines))