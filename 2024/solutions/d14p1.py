def simulate_robots(input_data: str, width: int = 101, height: int = 103, time: int = 100) -> int:
    robots = []

    for line in input_data.strip().split('\n'):
        p, v = line.split(' v=')
        px, py = map(int, p[2:].split(','))
        vx, vy = map(int, v.split(','))
        robots.append((px, py, vx, vy))

    final_positions = []
    for px, py, vx, vy in robots:
        new_x = (px + vx * time) % width
        new_y = (py + vy * time) % height
        final_positions.append((new_x, new_y))

    quadrants = [0, 0, 0, 0]
    not_counted = 0
    for x, y in final_positions:
        if x == width // 2 or y == height // 2:
            not_counted += 1
            continue
        if x < width // 2 and y < height // 2:
            quadrants[0] += 1
        elif x >= width // 2 and y < height // 2:
            quadrants[1] += 1
        elif x < width // 2 and y >= height // 2:
            quadrants[2] += 1
        elif x >= width // 2 and y >= height // 2:
            quadrants[3] += 1
    
    safety_factor = 1
    for count in quadrants:
        safety_factor *= count
    return safety_factor

input_data = open('../inputs/input14.txt', 'r').read()
print(simulate_robots(input_data))