import re

def solve_region(shapes: list[str], grid: str) -> int:
    sizes = [shape.count('#') for shape in shapes]
    count = 0
    for grid in grids.splitlines():
        width, height, *present_quantities = map(int, re.findall(r'\d+', grid))
        region_area = width * height

        presents_area = sum(quantity * area for quantity, area in zip(present_quantities, sizes))
        if region_area >= presents_area:
            count += 1
    return count

with open("../inputs/input12.txt") as file:
    *shapes, grids = file.read().split("\n\n")
print(solve_region(shapes, grids))