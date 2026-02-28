def solve_cephalopod_worksheet(worksheet: list[str]) -> int:
    rows = [row.split() for row in worksheet if row.strip()]
    num_problems = len(rows[-1])
    problems = []
    for col in range(num_problems):
        nums = []
        for row in rows[:-1]:
            if col < len(row):
                nums.append(int(row[col]))
        op = rows[-1][col]
        problems.append((nums, op))

    answers = []
    for nums, op in problems:
        result = 1
        if op == '+':
            result = sum(nums)
        elif op == '*':
            for num in nums:
                result *= num
        answers.append(result)
    return sum(answers)

with open("../inputs/input6.txt", "r") as file:
    worksheet = [line.strip() for line in file.readlines()]
print(solve_cephalopod_worksheet(worksheet))