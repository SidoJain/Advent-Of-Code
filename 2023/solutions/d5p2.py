def parseInput(filename: str):
    with open(filename) as file:
        blocks = file.read().strip().split('\n\n')

    seeds_line = blocks[0]
    seeds_raw = [int(x) for x in seeds_line.split(':')[1].split()]
    seeds = [[seeds_raw[i], seeds_raw[i] + seeds_raw[i+1]] for i in range(0, len(seeds_raw), 2)]

    maps = []
    for block in blocks[1:]:
        lines = block.split('\n')[1:]
        current_map = []
        for line in lines:
            if line.strip():
                dest_start, src_start, range_len = map(int, line.split())
                current_map.append([dest_start, src_start, src_start + range_len])
        maps.append(current_map)
    return seeds, maps

def findLowestLocation(seeds: list[list[int]], maps: list[list[list[int]]]) -> int:
    current_ranges = seeds
    for mapping in maps:
        new_ranges = []
        while current_ranges:
            r_start, r_end = current_ranges.pop()
            matched = False

            for dest_start, src_start, src_end in mapping:
                overlap_start = max(r_start, src_start)
                overlap_end = min(r_end, src_end)
                if overlap_start < overlap_end:
                    offset = dest_start - src_start
                    new_ranges.append([overlap_start + offset, overlap_end + offset])
                    if r_start < overlap_start:
                        current_ranges.append([r_start, overlap_start])
                    if r_end > overlap_end:
                        current_ranges.append([overlap_end, r_end])
                    matched = True
            if not matched:
                new_ranges.append([r_start, r_end])
        current_ranges = new_ranges
    return min(r[0] for r in current_ranges)

seeds, maps = parseInput('../inputs/input5.txt')
print(findLowestLocation(seeds, maps))