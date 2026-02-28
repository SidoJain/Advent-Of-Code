def parse_input(path: str) -> tuple[list[tuple[int, int]], list[int]]:
    with open(path, "r") as file:
        blocks = file.read().strip().split("\n\n")

    range_lines = blocks[0].splitlines()
    id_lines = blocks[1].splitlines()

    ranges = []
    for line in range_lines:
        start_str, end_str = line.split("-")
        ranges.append((int(start_str), int(end_str)))

    ids = [int(line) for line in id_lines]
    return ranges, ids

def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    ranges.sort(key=lambda x: x[0])
    merged = [ranges[0]]
    for current_start, current_end in ranges[1:]:
        last_start, last_end = merged[-1]
        if current_start <= last_end:
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            merged.append((current_start, current_end))
    return merged

def in_ranges(target: int, sorted_ranges: list[tuple[int, int]]) -> bool:
    low = 0
    high = len(sorted_ranges) - 1
    while low <= high:
        mid = (low + high) // 2
        start, end = sorted_ranges[mid]
        if start <= target <= end:
            return True
        elif target < start:
            high = mid - 1
        else:
            low = mid + 1
    return False

def count_fresh_ids(ranges: list[tuple[int, int]], ids: list[int]) -> int:
    merged_ranges = merge_ranges(ranges)
    count = 0
    for id in ids:
        if in_ranges(id, merged_ranges):
            count += 1
    return count

ranges, ids = parse_input("../inputs/input5.txt")
print(count_fresh_ids(ranges, ids))