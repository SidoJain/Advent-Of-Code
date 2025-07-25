from typing import Optional

def count_all_ways(design: str, patterns: set[str], memo: Optional[dict[str, int]] = None) -> int:
    if memo is None:
        memo = {}
    if not design:
        return 1
    if design in memo:
        return memo[design]

    total_ways = 0
    for pattern in patterns:
        if design.startswith(pattern):
            remaining = design[len(pattern):]
            total_ways += count_all_ways(remaining, patterns, memo)

    memo[design] = total_ways
    return total_ways

def parse_input(input_text: str) -> tuple[set[str], list[str]]:
    lines = input_text.strip().split('\n')
    patterns = {p.strip() for p in lines[0].split(',')}
    designs = [line.strip() for line in lines[2:] if line.strip()]

    return patterns, designs

def sum_all_possible_ways(patterns: set[str], designs: list[str]) -> int:
    total = 0
    memo = {}
    for design in designs:
        ways = count_all_ways(design, patterns, memo)
        if ways > 0:
            total += ways
    return total

raw_data = open('../inputs/input19.txt').read().strip()
patterns, designs = parse_input(raw_data)
result = sum_all_possible_ways(patterns, designs)
print(result)