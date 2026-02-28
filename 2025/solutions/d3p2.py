def max_k_digit(bank: str, k: int = 12) -> int:
    n = len(bank)
    stack = []
    digits_to_remove = n - k

    for digit in bank:
        while digits_to_remove > 0 and stack and stack[-1] < digit:
            stack.pop()
            digits_to_remove -= 1
        stack.append(digit)

    result_str = "".join(stack[:k])
    return int(result_str)

with open("../inputs/input3.txt", "r") as file:
    banks = [bank.strip() for bank in file.readlines()]
total_sum = sum([max_k_digit(bank, 12) for bank in banks])
print(total_sum)