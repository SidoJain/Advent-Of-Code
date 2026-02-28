def solve_cephalopod_worksheet(worksheet: list[str]) -> int:
    width = max(len(line) for line in worksheet)
    grid = [line.ljust(width) for line in worksheet]
    digit_rows = grid[:-1]
    op_row = grid[-1]

    total = 0
    cur_num = []
    cur_op = ""
    for col in range(width - 1, -1, -1):
        is_sep = True
        for row in grid:
            if row[col] != " ":
                is_sep = False
                break

        if is_sep:
            if cur_num:
                total += calculate_problem(cur_num, cur_op)
                cur_num = []
                cur_op = ""
            continue

        num_str = ""
        for row in digit_rows:
            char = row[col]
            if char.isdigit():
                num_str += char

        if num_str:
            cur_num.append(int(num_str))
        op_char = op_row[col]
        cur_op = op_char

    if cur_num:
        total += calculate_problem(cur_num, cur_op)
    return total

def calculate_problem(numbers: list[int], op: str) -> int:
    result = numbers[0]
    for num in numbers[1:]:
        if op == "+":
            result += num
        elif op == "*":
            result *= num
    return result

with open("../inputs/input6.txt", "r") as file:
    worksheet = file.readlines()
print(solve_cephalopod_worksheet(worksheet))