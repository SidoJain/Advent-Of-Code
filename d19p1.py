from typing import Optional

def can_make_design(design: str, patterns: set[str], memo: Optional[dict[str, bool]] = None) -> bool:
    if memo is None:
        memo = {}
    if not design:
        return True
    if design in memo:
        return memo[design]

    for pattern in patterns:
        if design.startswith(pattern):
            remaining = design[len(pattern):]
            if can_make_design(remaining, patterns, memo):
                memo[design] = True
                return True
    memo[design] = False
    return False

def parse_input(input_text: str) -> tuple[set[str], list[str]]:
    lines = input_text.strip().split('\n')
    patterns = {p.strip() for p in lines[0].split(',')}
    designs = [line.strip() for line in lines[2:] if line.strip()]
    
    return patterns, designs

def count_possible_designs(patterns: set[str], designs: list[str]) -> int:
    memo = {}
    possible_count = sum(1 for design in designs if can_make_design(design, patterns, memo))
    return possible_count

example_input = open('../inputs/input19.txt').read().strip()
patterns, designs = parse_input(example_input)
result = count_possible_designs(patterns, designs)
print(result)