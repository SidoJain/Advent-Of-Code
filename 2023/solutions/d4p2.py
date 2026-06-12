def parseInput(filename: str) -> list[str]:
    with open(filename) as file:
        return [line.strip().split(': ')[1] for line in file.readlines()]

def countMatches(line: str) -> int:
    winning, ours = line.split(' | ')
    winning_set = {int(num) for num in winning.split()}
    ours_set = {int(num) for num in ours.split()}
    return len(winning_set.intersection(ours_set))

def countTotalCards(lines: list[str]) -> int:
    card_counts = {i: 1 for i in range(len(lines))}
    for i, line in enumerate(lines):
        matches = countMatches(line)
        for j in range(1, matches + 1):
                card_counts[i + j] += card_counts[i]
    return sum(card_counts.values())

lines = parseInput('../inputs/input4.txt')
print(countTotalCards(lines))