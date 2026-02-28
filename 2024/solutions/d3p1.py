def readFile(filename: str) -> str:
    with open(filename) as f:
        return f.read().replace('\n', '')

def solve(raw_data: str) -> int:
    sum = 0

    while raw_data.find('mul(') != -1:
        start = raw_data.find('mul(')
        end = raw_data.find(')', start)
        if end > 11 + start:
            raw_data = raw_data.replace('mul(', '', 1)
            continue
        if end == -1:
            break

        substring = raw_data[start : end + 1]
        splitSub = substring.replace('mul(', '').replace(')', '').split(',')
        if len(splitSub) != 2 or (splitSub[0]).isnumeric() == False or (splitSub[1]).isnumeric() == False:
            raw_data = raw_data.replace('mul(', '', 1)
            continue
        sum += int(splitSub[0]) * int(splitSub[1])
        raw_data = raw_data.replace(substring, '')
    return sum

raw_data = readFile('../inputs/input3.txt')
sum = solve(raw_data)
print(sum)