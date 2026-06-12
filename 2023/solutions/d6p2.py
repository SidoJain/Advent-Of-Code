import math

def parseInput(filename: str) -> tuple[int, int]:
    with open(filename) as file:
        time, dist = file.readlines()
        time = int("".join(time.strip().split()[1:]))
        dist = int("".join(dist.strip().split()[1:]))
    return time, dist

def countWaysToWin(time: int, dist: int) -> int:
    discriminant = time ** 2 - 4 * dist
    root1 = (time - math.sqrt(discriminant)) / 2
    root2 = (time + math.sqrt(discriminant)) / 2
    min_hold = math.floor(root1) + 1
    max_hold = math.ceil(root2) - 1
    return max_hold - min_hold + 1

time, dist = parseInput('../inputs/input6.txt')
print(countWaysToWin(time, dist))