def parse_ranges(ranges_str: str) -> list[tuple[int, int]]:
    ranges = []
    for range in ranges_str.split(','):
        start, end = range.split('-')
        ranges.append((int(start), int(end)))
    return ranges

def sum_invalid_ids(ranges: list[tuple[int, int]]) -> int:
    total_sum = 0
    for start, end in ranges:
        len_start = len(str(start))
        len_end = len(str(end))

        for length in range(len_start, len_end + 1):
            if length % 2 != 0:
                continue

            multiplier = 10 ** (length // 2) + 1
            min_x_digits = 10 ** ((length // 2) - 1)
            max_x_digits = 10 ** (length // 2) - 1
            val_lower = (start + multiplier - 1) // multiplier
            val_upper = end // multiplier

            actual_lower = max(val_lower, min_x_digits)
            actual_upper = min(val_upper, max_x_digits)
            if actual_lower <= actual_upper:
                count = actual_upper - actual_lower + 1
                sum_x = count * (actual_lower + actual_upper) // 2
                total_sum += sum_x * multiplier
    return total_sum

with open("../inputs/input2.txt", "r") as file:
    input_ranges = file.read()

ranges = parse_ranges(input_ranges)
result = sum_invalid_ids(ranges)
print(result)