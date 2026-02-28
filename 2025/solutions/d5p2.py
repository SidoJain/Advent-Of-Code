def parse_input(path: str) -> list[tuple[int, int]]:
    with open(path, "r") as file:
        first_block = file.read().strip().split("\n\n")[0]
    return [(int(line.split("-")[0]), int(line.split("-")[1])) for line in first_block.splitlines()]

def count_unique_fresh_ids(ranges: list[tuple[int, int]]) -> int:
    ranges.sort()
    merged = []
    current_start, current_end = ranges[0]
    for start, end in ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end

    merged.append((current_start, current_end))
    return sum(end - start + 1 for start, end in merged)

ranges = parse_input("../inputs/input5.txt")
print(count_unique_fresh_ids(ranges))