def parseInput(filename: str) -> list[str]:
    with open(filename) as file:
        line = file.readline()
        return line.strip().split(',')

def getHash(label: str) -> int:
    cur_score = 0
    for char in label:
        cur_score += ord(char)
        cur_score *= 17
        cur_score %= 256
    return cur_score

def countScore(seqs: list[str]) -> int:
    total_score = 0
    for seq in seqs:
        total_score += getHash(seq)
    return total_score

seqs = parseInput('../inputs/input15.txt')
print(countScore(seqs))