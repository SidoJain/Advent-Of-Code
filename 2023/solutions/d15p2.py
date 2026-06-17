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

def calcFocucingPower(seqs: list[str]) -> int:
    boxes = [{} for _ in range(256)]
    for seq in seqs:
        if '-' in seq:
            label = seq[:-1]
            box_idx = getHash(label)
            if label in boxes[box_idx]:
                del boxes[box_idx][label]
        elif '=' in seq:
            label, focal_str = seq.split('=')
            box_idx = getHash(label)
            focal_length = int(focal_str)
            boxes[box_idx][label] = focal_length

    total_power = 0
    for box_idx, box in enumerate(boxes):
        for slot_idx, (label, focal_length) in enumerate(box.items(), start=1):
            power = (box_idx + 1) * slot_idx * focal_length
            total_power += power
    return total_power

seqs = parseInput('../inputs/input15.txt')
print(calcFocucingPower(seqs))