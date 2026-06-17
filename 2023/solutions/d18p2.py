def parseInput(filename: str) -> list[tuple[str, int]]:
    real_instructions = []
    dir_mapping = {
        '0': 'R',
        '1': 'D',
        '2': 'L',
        '3': 'U'
    }

    with open(filename) as file:
        for line in file:
            parts = line.strip().split()
            hex_code = parts[2]
            hex_clean = hex_code.replace('(', '').replace(')', '').replace('#', '')
            distance = int(hex_clean[:5], 16)
            direction = dir_mapping[hex_clean[5]]
            real_instructions.append((direction, distance))
    return real_instructions

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

true_instructions = parseInput('../inputs/input18.txt')
print(calcLagoonVolume(true_instructions))