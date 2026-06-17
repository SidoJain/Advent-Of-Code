def parseInput(filename: str) -> list[tuple[str, int]]:
    instructions = []
    with open(filename) as file:
        for line in file:
            parts = line.strip().split()
            instructions.append((parts[0], int(parts[1])))
    return instructions

def calcLagoonVolume(instructions: list[tuple[str, int]]) -> int:
    dirs = {
        'R': (0, 1),
        'L': (0, -1),
        'U': (-1, 0),
        'D': (1, 0)
    }

    vertices = [(0, 0)]
    boundary_points = 0
    r, c = 0, 0

    for direction, steps in instructions:
        dr, dc = dirs[direction]
        r += dr * steps
        c += dc * steps
        vertices.append((r, c))
        boundary_points += steps

    area = 0
    for i in range(len(vertices) - 1):
        r1, c1 = vertices[i]
        r2, c2 = vertices[i + 1]
        area += (r1 * c2) - (r2 * c1)
    area = abs(area) // 2

    total_volume = area + (boundary_points // 2) + 1
    return total_volume

instructions = parseInput('../inputs/input18.txt')
print(calcLagoonVolume(instructions))