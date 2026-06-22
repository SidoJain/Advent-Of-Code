def parseInput(filename: str) -> list[tuple[tuple[int, int, int], tuple[int, int, int]]]:
    hailstones = []
    with open(filename) as file:
        for line in file:
            pos_str, vel_str = line.strip().split(" @ ")
            px, py, pz = map(int, pos_str.split(", "))
            vx, vy, vz = map(int, vel_str.split(", "))
            hailstones.append(((px, py, pz), (vx, vy, vz)))
    return hailstones

def countFutureIntersections(hailstones: list[tuple[tuple[int, int, int], tuple[int, int, int]]], min_val: int, max_val: int) -> int:
    lines = []
    for pos, vel in hailstones:
        px, py, _ = pos
        vx, vy, _ = vel
        A = vy
        B = -vx
        C = vy * px - vx * py
        lines.append(((px, py, vx, vy), A, B, C))

    intersect_count = 0
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            h1, A1, B1, C1 = lines[i]
            h2, A2, B2, C2 = lines[j]

            D = A1 * B2 - A2 * B1
            if D == 0:
                continue 

            ix = (C1 * B2 - C2 * B1) / D
            iy = (A1 * C2 - A2 * C1) / D
            if min_val <= ix <= max_val and min_val <= iy <= max_val:
                px1, py1, vx1, vy1 = h1
                px2, py2, vx2, vy2 = h2
                if vx1 != 0:
                    t1 = (ix - px1) / vx1
                else:
                    t1 = (iy - py1) / vy1

                if vx2 != 0:
                    t2 = (ix - px2) / vx2
                else:
                    t2 = (iy - py2) / vy2

                if t1 >= 0 and t2 >= 0:
                    intersect_count += 1
    return intersect_count

if __name__ == '__main__':
    hailstones = parseInput('../inputs/input24.txt')

    MIN_BOUND = 200000000000000
    MAX_BOUND = 400000000000000
    print(countFutureIntersections(hailstones, MIN_BOUND, MAX_BOUND))