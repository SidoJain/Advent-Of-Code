def run_program(registers: tuple[int, int, int], program: list[int]) -> str:
    A, B, C = registers
    instruction_pointer = 0
    output = []

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

    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]
        instruction_pointer += 2

        match(opcode):
            case 0:     # adv
                A //= 2 ** resolve_combo_operand(operand)
            case 1:     # bxl
                B ^= operand
            case 2:     # bst
                B = resolve_combo_operand(operand) % 8
            case 3:     # jnz
                if A != 0:
                    instruction_pointer = operand
            case 4:     # bxc
                B ^= C
            case 5:     # out
                output.append(resolve_combo_operand(operand) % 8)
            case 6:     # bdv
                B = A // (2 ** resolve_combo_operand(operand))
            case 7:     # cdv
                C = A // (2 ** resolve_combo_operand(operand))
    return ','.join(map(str, output))

registers = (46337277, 0, 0)
program = [2, 4, 1, 1, 7, 5, 4, 4, 1, 4, 0, 3, 5, 5, 3, 0]
result = run_program(registers, program)
print('Output:', result)