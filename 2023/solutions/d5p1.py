def parseInput(filename: str) -> tuple[list[int], list[list[tuple[int, int, int]]]]:
    with open(filename) as file:
        blocks = file.read().strip().split('\n\n')

    seeds_line = blocks[0]
    seeds = [int(x) for x in seeds_line.split(':')[1].split()]

    maps = []
    for block in blocks[1:]:
        lines = block.split('\n')[1:]
        current_map = []
        for line in lines:
            if line.strip():
                dest_start, src_start, range_len = map(int, line.split())
                current_map.append((dest_start, src_start, range_len))
        maps.append(current_map)
    return seeds, maps

def applyMap(value: int, mapping: list[tuple[int, int, int]]) -> int:
    for dest_start, src_start, range_len in mapping:
        if src_start <= value < src_start + range_len:
            return dest_start + (value - src_start)
    return value

def findLowestLocation(seeds: list[int], maps: list[list[tuple[int, int, int]]]) -> float:
    lowest_location = float('inf')
    for seed in seeds:
        current_val = seed
        for mapping in maps:
            current_val = applyMap(current_val, mapping)

        if current_val < lowest_location:
            lowest_location = current_val
    return lowest_location

seeds, maps = parseInput('../inputs/input5.txt')
print(findLowestLocation(seeds, maps))