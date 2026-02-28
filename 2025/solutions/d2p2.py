def parse_ranges(ranges_str: str) -> list[tuple[int, int]]:
    ranges = []
    for range in ranges_str.split(','):
        start, end = range.split('-')
        ranges.append((int(start), int(end)))
    return ranges

def get_divisors(n: int) -> list[int]:
    divs = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if i * i != n:
                divs.append(n // i)
    return [d for d in divs if d <= n // 2]

def sum_invalid_ids(ranges: list[tuple[int, int]]) -> int:
    unique_invalid_ids = set()
    for start, end in ranges:
        len_start = len(str(start))
        len_end = len(str(end))

        for num_len in range(len_start, len_end + 1):
            for pattern_len in get_divisors(num_len):
                multiplier = (10 ** num_len - 1) // (10 ** pattern_len - 1)
                min_x_digits = 10 ** (pattern_len - 1)
                max_x_digits = 10 ** pattern_len - 1
                x_lower_bound = (start + multiplier - 1) // multiplier
                x_upper_bound = end // multiplier

                actual_min = max(min_x_digits, x_lower_bound)
                actual_max = min(max_x_digits, x_upper_bound)
                if actual_min <= actual_max:
                    for x in range(actual_min, actual_max + 1):
                        unique_invalid_ids.add(x * multiplier)
    return sum(unique_invalid_ids)

with open("../inputs/input2.txt", "r") as file:
    input_ranges = file.read()

ranges = parse_ranges(input_ranges)
result = sum_invalid_ids(ranges)
print(result)