from z3 import Int, Solver, sat

def parseInput(filename: str) -> list[tuple[tuple[int, int, int], tuple[int, int, int]]]:
    hailstones = []
    with open(filename) as file:
        for line in file:
            pos_str, vel_str = line.strip().split(" @ ")
            px, py, pz = map(int, pos_str.split(", "))
            vx, vy, vz = map(int, vel_str.split(", "))
            hailstones.append(((px, py, pz), (vx, vy, vz)))
    return hailstones

def throwMagicRock(hailstones: list[tuple[tuple[int, int, int], tuple[int, int, int]]]) -> int:
    solver = Solver()

    xr = Int('xr')
    yr = Int('yr')
    zr = Int('zr')
    vxr = Int('vxr')
    vyr = Int('vyr')
    vzr = Int('vzr')

    for i in range(3):
        pos, vel = hailstones[i]
        px, py, pz = pos
        vx, vy, vz = vel

        t = Int(f't_{i}')
        solver.add(t >= 0)
        solver.add(xr + vxr * t == px + vx * t)
        solver.add(yr + vyr * t == py + vy * t)
        solver.add(zr + vzr * t == pz + vz * t)

    if solver.check() == sat:
        pass
    else:
        raise Exception("The solver could not find a solution.")

    model = solver.model()

    ans_x = model.eval(xr).as_long()
    ans_y = model.eval(yr).as_long()
    ans_z = model.eval(zr).as_long()
    return ans_x + ans_y + ans_z

hailstones = parseInput('../inputs/input24.txt')
print(throwMagicRock(hailstones))