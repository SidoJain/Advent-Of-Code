def max_two_digit(bank: str) -> int:
    n = len(bank)
    max_right = int(bank[-1])
    best = 0

    for i in range(n - 2, -1, -1):
        digit = int(bank[i])
        current_val = digit * 10 + max_right
        if current_val > best:
            best = current_val
            if best == 99:
                return 99
        if digit > max_right:
            max_right = digit
    return best

with open("../inputs/input3.txt", "r") as file:
    banks = [bank.strip() for bank in file.readlines()]
total_sum = sum([max_two_digit(bank) for bank in banks])
print(total_sum)