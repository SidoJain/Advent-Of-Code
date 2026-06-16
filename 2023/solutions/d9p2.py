def parseInput(filename: str) -> list[list[int]]:
    with open(filename, 'r') as file:
        return [[int(x) for x in line.strip().split()] for line in file.readlines()]

def extrapolatePreviousValue(histories: list[list[int]]) -> int:
    total_extrapolated_sum = 0
    for history in histories:
        sequences = [history]
        while not all(x == 0 for x in sequences[-1]):
            current_seq = sequences[-1]
            next_seq = [current_seq[i + 1] - current_seq[i] for i in range(len(current_seq) - 1)]
            sequences.append(next_seq)

        prev_val = 0
        for i in range(len(sequences) - 2, -1, -1):
            prev_val = sequences[i][0] - prev_val
        total_extrapolated_sum += prev_val
    return total_extrapolated_sum

histories = parseInput('../inputs/input9.txt')
print(extrapolatePreviousValue(histories))