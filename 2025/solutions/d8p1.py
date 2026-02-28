Coord = tuple[int, int, int]
Edge = tuple[int, int, int]

def parse_input(raw_data: str) -> list[Coord]:
    points = []
    lines = raw_data.strip().split('\n')
    for line in lines:
        parts = line.split(',')
        points.append((int(parts[0]), int(parts[1]), int(parts[2])))
    return points

def dist_sq(p1: Coord, p2: Coord) -> int:
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    dz = p1[2] - p2[2]
    return dx * dx + dy * dy + dz * dz

def get_all_edges(points: list[Coord]) -> list[Edge]:
    edges = []
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            d = dist_sq(points[i], points[j])
            edges.append((d, i, j))
    return edges

def make_set(n: int) -> list[int]:
    return list(range(n))

def find(parent: list[int], i: int) -> int:
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent: list[int], i: int, j: int) -> None:
    root_i = find(parent, i)
    root_j = find(parent, j)
    if root_i != root_j:
        parent[root_i] = root_j

def solve_circuit(input_str: str, limit: int) -> int:
    points = parse_input(input_str)
    n = len(points)

    all_edges = get_all_edges(points)
    all_edges.sort(key=lambda x: x[0])
    edges_to_process = all_edges[:min(len(all_edges), limit)]
    parent = make_set(n)
    for _, u, v in edges_to_process:
        union(parent, u, v)

    size_map = {}
    for i in range(n):
        root = find(parent, i)
        if root in size_map:
            size_map[root] += 1
        else:
            size_map[root] = 1

    sizes = list(size_map.values())
    sizes.sort(reverse=True)
    result = 1
    for size in sizes[:3]:
        result *= size
    return result

with open("../inputs/input8.txt", "r") as file:
    data = file.read()
print(solve_circuit(data, 1000))