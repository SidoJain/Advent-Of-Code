def parseInput(filename: str) -> list[list[int]]:
    with open(filename, 'r') as file:
        return [[int(x) for x in line.strip().split()] for line in file.readlines()]

def extrapolateNextValue(histories: list[list[int]]) -> int:
    total_extrapolated_sum = 0
    for history in histories:
        sequences = [history]
        while not all(x == 0 for x in sequences[-1]):
            current_seq = sequences[-1]
            next_seq = [current_seq[i + 1] - current_seq[i] for i in range(len(current_seq) - 1)]
            sequences.append(next_seq)
        next_val = sum(seq[-1] for seq in sequences)
        total_extrapolated_sum += next_val
    return total_extrapolated_sum

histories = parseInput('../inputs/input9.txt')
print(extrapolateNextValue(histories))