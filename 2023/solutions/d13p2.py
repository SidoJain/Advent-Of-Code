def parseInput(filename: str) -> list[list[str]]:
    with open(filename, 'r') as file:
        content = file.read().strip()
    return [pattern.split('\n') for pattern in content.split('\n\n')]

def findReflectionLine(lines: list[str], expected_smudges: int) -> int:
    for i in range(1, len(lines)):
        smudges = 0
        check_range = min(i, len(lines) - i)
        for j in range(check_range):
            row1 = lines[i - 1 - j]
            row2 = lines[i + j]
            smudges += sum(1 for a, b in zip(row1, row2) if a != b)
            if smudges > expected_smudges:
                break

        if smudges == expected_smudges:
            return i
    return 0

def summarizeNotes(patterns: list[list[str]]) -> int:
    total_summary = 0
    for pattern in patterns:
        horizontal_val = findReflectionLine(pattern, 1)
        if horizontal_val > 0:
            total_summary += (100 * horizontal_val)
            continue

        transposed_pattern = [''.join(col) for col in zip(*pattern)]
        vertical_val = findReflectionLine(transposed_pattern, 1)
        if vertical_val > 0:
            total_summary += vertical_val
    return total_summary

patterns = parseInput('../inputs/input13.txt')
print(summarizeNotes(patterns))