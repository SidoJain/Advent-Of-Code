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
    for read_pos in range(len(blocks)):
        if blocks[read_pos] == -1:
            swap_pos = len(blocks) - 1
            while blocks[swap_pos] == -1:
                swap_pos -= 1
            if swap_pos <= read_pos:
                break
            blocks[read_pos], blocks[swap_pos] = blocks[swap_pos], blocks[read_pos]
    return blocks

def calculate_checksum(blocks: list[int]) -> int:
    return sum(position * block_id for position, block_id in enumerate(blocks) if block_id != -1)

def solve_disk_fragmenter(disk_map: str) -> int:
    blocks = parse_disk_map(disk_map)
    blocks = compact_blocks(blocks)
    return calculate_checksum(blocks)

raw_data = open('../inputs/input9.txt').read()
result = solve_disk_fragmenter(raw_data)
print(result)