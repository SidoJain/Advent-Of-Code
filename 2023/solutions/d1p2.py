def parseInput(filename: str) -> list[str]:
    with open(filename) as file:
        return file.readlines()

def getSum(line: str) -> int:
    word_to_digit = {
        "one": "1", "two": "2", "three": "3", 
        "four": "4", "five": "5", "six": "6", 
        "seven": "7", "eight": "8", "nine": "9"
    }

    digits = []
    for i in range(len(line)):
        if line[i] >= '0' and line[i] <= '9':
            digits.append(line[i])
        else:
            for word, digit in word_to_digit.items():
                if line[i:].startswith(word):
                    digits.append(digit)
                    break
    return int(digits[0] + digits[-1])

def getSums(lines: list[str]) -> int:
    total_sum = 0
    for line in lines:
        total_sum += getSum(line)
    return total_sum

lines = parseInput('../inputs/input1.txt')
print(getSums(lines))