Point = tuple[int, int]
Edge = tuple[int, int, int, int]
RectBounds = tuple[int, int, int, int]

def check_vertex_overlap(rect_bounds: RectBounds, points: list[Point]) -> bool:
    rx1, rx2, ry1, ry2 = rect_bounds
    for px, py in points:
        if rx1 < px < rx2 and ry1 < py < ry2:
            return True
    return False

def check_edge_crossing(rect_bounds: RectBounds, edges: list[Edge]) -> bool:
    rx1, rx2, ry1, ry2 = rect_bounds
    for ex1, ey1, ex2, ey2 in edges:
        if ex1 == ex2: 
            if rx1 < ex1 < rx2:
                edge_y_min, edge_y_max = min(ey1, ey2), max(ey1, ey2)
                if edge_y_min <= ry1 and edge_y_max >= ry2:
                    return True
        else:
            if ry1 < ey1 < ry2:
                edge_x_min, edge_x_max = min(ex1, ex2), max(ex1, ex2)
                if edge_x_min <= rx1 and edge_x_max >= rx2:
                    return True
    return False

def find_largest_polygon(data: str) -> int:
    points = []
    for line in data.strip().splitlines():
        parts = line.split(',')
        points.append((int(parts[0]), int(parts[1])))

    n = len(points)
    edges = []
    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n]
        edges.append((p1[0], p1[1], p2[0], p2[1]))

    max_area = 0
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            rx1, rx2 = min(x1, x2), max(x1, x2)
            ry1, ry2 = min(y1, y2), max(y1, y2)

            width = rx2 - rx1 + 1
            height = ry2 - ry1 + 1
            area = width * height
            if area <= max_area:
                continue

            rect_bounds: RectBounds = (rx1, rx2, ry1, ry2)
            if check_vertex_overlap(rect_bounds, points):
                continue
            if check_edge_crossing(rect_bounds, edges):
                continue
            max_area = area
    return max_area

with open("../inputs/input9.txt", "r") as file:
    data = file.read()
print(find_largest_polygon(data))