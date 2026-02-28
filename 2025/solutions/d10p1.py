from collections import deque

def min_presses_for_lights(line: str) -> int:
    diagram, *buttons, _ = line.split(" ")
    target_str = diagram[1:-1]
    target_mask = 0
    for i, char in enumerate(target_str):
        if char == '#':
            target_mask |= (1 << i)

    button_masks = []
    for button in buttons:
        content = button[1:-1]
        indices = [int(x) for x in content.split(",")]

        mask = 0
        for idx in indices:
            mask |= (1 << idx)
        button_masks.append(mask)

    queue = deque([(0, 0)])
    visited = {0}
    while queue:
        current_state, presses = queue.popleft()
        if current_state == target_mask:
            return presses

        for btn_mask in button_masks:
            next_state = current_state ^ btn_mask
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, presses + 1))
    return -1

with open("../inputs/input10.txt") as file:
    data = [line.strip() for line in file.readlines()]
print(sum(min_presses_for_lights(line) for line in data))