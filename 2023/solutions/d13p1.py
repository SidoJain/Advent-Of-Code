def parseInput(filename: str) -> list[list[str]]:
    with open(filename, 'r') as file:
        content = file.read().strip()
    return [pattern.split('\n') for pattern in content.split('\n\n')]

def findReflectionLine(lines: list[str]) -> int:
    for i in range(1, len(lines)):
        is_reflection = True
        check_range = min(i, len(lines) - i)
        for j in range(check_range):
            if lines[i - 1 - j] != lines[i + j]:
                is_reflection = False
                break

        if is_reflection:
            return i
    return 0

def summarizeNotes(patterns: list[list[str]]) -> int:
    total_summary = 0
    for pattern in patterns:
        horizontal_val = findReflectionLine(pattern)
        if horizontal_val > 0:
            total_summary += (100 * horizontal_val)
            continue

        transposed_pattern = [''.join(col) for col in zip(*pattern)]
        vertical_val = findReflectionLine(transposed_pattern)
        if vertical_val > 0:
            total_summary += vertical_val
    return total_summary

patterns = parseInput('../inputs/input13.txt')
print(summarizeNotes(patterns))