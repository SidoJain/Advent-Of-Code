def parse_disk_map(disk_map: str) -> list[int]:
    blocks = []
    id = 0
    for i in range(0, len(disk_map)):
        if i % 2 == 0:
            file_size = int(disk_map[i])
            blocks.extend([id] * file_size)
            id += 1
        else:
            free_size = int(disk_map[i])
            blocks.extend([-1] * free_size)
    return blocks

def compact_blocks(blocks: list[int]) -> list[int]:
    max_id = max(blocks)
    block_len = len(blocks)

    for file_id in range(max_id, -1, -1):
        file_positions = [i for i, block in enumerate(blocks) if block == file_id]
        if not file_positions:
            continue

        file_length = len(file_positions)
        free_space_idx = -1
        free_space_len = 0
        for i in range(block_len):
            if blocks[i] == -1:
                if free_space_idx == -1:
                    free_space_idx = i
                free_space_len += 1
                if free_space_len == file_length:
                    if free_space_idx < file_positions[0]:
                        for pos in file_positions:
                            blocks[pos] = -1

                        for j in range(file_length):
                            blocks[free_space_idx + j] = file_id
                    break
            else:
                free_space_idx = -1
                free_space_len = 0
    return blocks

def calculate_checksum(blocks: list[int]) -> int:
    return sum(position * block_id for position, block_id in enumerate(blocks) if block_id != -1)

def solve_disk_fragmenter(disk_map: str) -> int:
    blocks = parse_disk_map(disk_map)
    blocks = compact_blocks(blocks)
    return calculate_checksum(blocks)

raw_data = open('../inputs/input9.txt').read().strip()
result = solve_disk_fragmenter(raw_data)
print(result)