def find_largest_rectangle(input_data: str) -> int:
    coords = []
    for line in input_data.strip().splitlines():
        x_str, y_str = line.split(',')
        coords.append((int(x_str), int(y_str)))

    max_area = 0
    n = len(coords)
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = coords[i]
            x2, y2 = coords[j]

            width = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1
            area = width * height
            if area > max_area:
                max_area = area
    return max_area

with open("../inputs/input9.txt", "r") as file:
    data = file.read()
print(find_largest_rectangle(data))