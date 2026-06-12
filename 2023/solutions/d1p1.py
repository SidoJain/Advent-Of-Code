def parseInput(filename: str) -> list[str]:
    with open(filename) as file:
        return file.readlines()

def getSum(line: str) -> int:
    left = 0
    right = len(line) - 1
    first_digit = ""
    last_digit = ""

    while left < len(line) and not first_digit:
        if line[left].isdigit():
            first_digit = line[left]
        else:
            left += 1

    while right >= 0 and not last_digit:
        if line[right].isdigit():
            last_digit = line[right]
        else:
            right -= 1

    if first_digit and last_digit:
        return int(first_digit + last_digit)
    return 0

def getSums(lines: list[str]) -> int:
    total_sum = 0
    for line in lines:
        total_sum += getSum(line)
    return total_sum

lines = parseInput('../inputs/input1.txt')
print(getSums(lines))