def parse_schematic(lines: list[str]) -> list[int]:
    heights = []
    max_height = len(lines) - 1
    
    for col in range(len(lines[0])):
        count = 0
        is_lock = lines[0][col] == '#'
        
        if is_lock:
            last_hash = 0
            for row in range(max_height + 1):
                if lines[row][col] == '#':
                    last_hash = row
            count = last_hash + 1
        else:
            first_hash = max_height
            for row in range(max_height, -1, -1):
                if lines[row][col] == '#':
                    first_hash = row
            count = max_height - first_hash + 1
        heights.append(count)
    return heights

def can_fit(lock_heights: list[int], key_heights: list[int]) -> bool:
    if len(lock_heights) != len(key_heights):
        return False
    
    max_height = 7
    for lock_h, key_h in zip(lock_heights, key_heights):
        if lock_h + key_h > max_height:
            return False
    return True

def solve_lock_puzzle(input_text: str) -> int:
    schematics = input_text.strip().split('\n\n')
    locks = []
    keys = []

    for schematic in schematics:
        lines = schematic.strip().split('\n')
        heights = parse_schematic(lines)
        if lines[0][0] == '#':
            locks.append(heights)
        else:
            keys.append(heights)

    compatible_pairs_count = 0
    for lock in locks:
        for key in keys:
            if can_fit(lock, key):
                compatible_pairs_count += 1
    return compatible_pairs_count

raw_data = open('../inputs/input25.txt').read()
result = solve_lock_puzzle(raw_data)
print(result)