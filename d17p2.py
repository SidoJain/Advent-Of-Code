def simulate(reg_a: int) -> list[int]:
    def resolve_combo_operand(operand: int) -> int:
        if operand <= 3:
            return operand
        elif operand == 4:
            return A
        elif operand == 5:
            return B
        elif operand == 6:
            return C
        return 0

    global best
    A = reg_a
    B = 0
    C = 0
    input = 0
    output = []
    while True:
        if input >= len(program):
            return output

        command = program[input]
        operand = program[input + 1]
        combo = resolve_combo_operand(operand)

        match command:
            case 0:     # adv
                A //= 2 ** combo
                input += 2
            case 1:     # bxl
                B ^= operand
                input += 2
            case 2:     # bst
                B = combo % 8
                input += 2
            case 3:     # jnz
                if A != 0:
                    input = operand
                else:
                    input += 2
            case 4:     # bxc
                B ^= C
                input += 2
            case 5:     # out
                output.append(combo % 8)
                if output[-1] != program[len(output) - 1]:
                    if len(output) > best:
                        best = len(output)
                        print(reg_a, oct(reg_a))
                    return output
                input += 2
            case 6:     # bdv
                B = A // (2 ** combo)
                input += 2
            case 7:     # cdv
                C = A // (2 ** combo)
                input += 2

A, B, C = 46337277, 0, 0
program = [2, 4, 1, 1, 7, 5, 4, 4, 1, 4, 0, 3, 5, 5, 3, 0]

reg_a = 0
best = 0
while True:
    reg_a += 1
    # A = reg_a * 8 ** 5 + 0o25052
    # A = reg_a * 8 ** 7 + 0o4025052
    A = reg_a * 8 ** 10 + 0o6274025052
    output = simulate(A)
    if output == program:
        print(f'Least A: {A}')
        break