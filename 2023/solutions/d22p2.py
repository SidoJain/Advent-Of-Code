from collections import deque

def parseInput(filename: str) -> list[list[int]]:
    bricks = []
    with open(filename) as file:
        for line in file:
            p1, p2 = line.strip().split('~')
            x1, y1, z1 = map(int, p1.split(','))
            x2, y2, z2 = map(int, p2.split(','))

            bricks.append([
                min(x1, x2), min(y1, y2), min(z1, z2),
                max(x1, x2), max(y1, y2), max(z1, z2)
            ])
    return bricks

def calculateTotalChainReactions(bricks: list[list[int]]) -> int:
    bricks.sort(key=lambda b: b[2])
    highest = {}
    supports = {i: set() for i in range(len(bricks))}
    supported_by = {i: set() for i in range(len(bricks))}
    for i, b in enumerate(bricks):
        x1, y1, z1, x2, y2, _ = b
        max_z_below = 0
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                z, _ = highest.get((x, y), (0, -1))
                if z > max_z_below:
                    max_z_below = z

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                z, owner_id = highest.get((x, y), (0, -1))
                if z == max_z_below and owner_id != -1:
                    supports[owner_id].add(i)
                    supported_by[i].add(owner_id)

        fall_distance = z1 - (max_z_below + 1)
        b[2] -= fall_distance
        b[5] -= fall_distance
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                highest[(x, y)] = (b[5], i)

    total_falling_bricks = 0
    for i in range(len(bricks)):
        falling = {i}
        queue = deque(supports[i])
        while queue:
            candidate = queue.popleft()
            if candidate in falling:
                continue

            if supported_by[candidate].issubset(falling):
                falling.add(candidate)
                for next_brick in supports[candidate]:
                    queue.append(next_brick)
        total_falling_bricks += len(falling) - 1
    return total_falling_bricks

bricks = parseInput('../inputs/input22.txt')
print(calculateTotalChainReactions(bricks))