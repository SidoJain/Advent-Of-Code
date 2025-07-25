import re

def readFile(filename: str) -> str:
    with open(filename) as f:
        return f.read().replace('\n', '')

def solve(raw_data: str) -> int:
    total_sum = 0
    do_enabled = True

    do_regex = r'do\(\)'
    dont_regex = r"don't\(\)"
    mul_regex = r'mul\((\d+),(\d+)\)'

    while raw_data:
        do_match = re.search(do_regex, raw_data)
        dont_match = re.search(dont_regex, raw_data)
        mul_match = re.search(mul_regex, raw_data)

        next_op = min([(do_match, 'do'), (dont_match, 'dont'), (mul_match, 'mul')], key=lambda x: x[0].start() if x[0] else float('inf'))
        if next_op[0] is None:
            break

        op_type = next_op[1]
        start, end = next_op[0].span()

        if op_type == 'do':
            do_enabled = True
        elif op_type == 'dont':
            do_enabled = False
        elif op_type == 'mul' and do_enabled:
            x, y = map(int, next_op[0].groups())
            total_sum += x * y
        raw_data = raw_data[end:]
    return total_sum

raw_data = readFile('../inputs/input3.txt')
total_sum = solve(raw_data)
print(total_sum)