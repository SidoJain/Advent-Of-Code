def parse_rotations(lines: list[str]) -> list[tuple[str, int]]:
    rotations = []
    for line in lines:
        line = line.strip()
        dir = line[0]
        dist = int(line[1:])
        rotations.append((dir, dist))
    return rotations

def safe_password(rotations: list[tuple[str, int]], start: int = 50) -> int:
    pos = start
    zeros = 0
    for dir, dist in rotations:
        if dir == "R":
            target = pos + dist
            count = (target // 100) - (pos // 100)
            zeros += count
            pos = target % 100
        else:
            target = pos - dist
            count = ((pos - 1) // 100) - ((target - 1) // 100)
            zeros += count
            pos = target % 100
    return zeros

with open("../inputs/input1.txt", "r") as file:
    lines = file.readlines()

rotations = parse_rotations(lines)
password = safe_password(rotations)
print(password)