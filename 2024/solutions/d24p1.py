def parse_input(raw_input: str) -> tuple[dict[str, int], list[tuple[str, str]]]:
    lines = raw_input.strip().split('\n')
    values = {}
    gates = []

    for line in lines:
        if ':' in line:
            wire, value = line.split(':')
            values[wire.strip()] = int(value.strip())
        elif '->' in line:
            gate, output = line.split('->')
            gates.append((gate.strip(), output.strip()))
    return values, gates

def evaluate_gate(gate: str, values: dict[str, int]) -> int | None:
    parts = gate.split()
    if len(parts) == 3:
        input1, operation, input2 = parts
        val1 = values.get(input1)
        val2 = values.get(input2)
        if val1 is None or val2 is None:
            return None

        if operation == 'AND':
            return val1 & val2
        elif operation == 'OR':
            return val1 | val2
        elif operation == 'XOR':
            return val1 ^ val2
    return None

def simulate(gates: list[tuple[str, str]], values: dict[str, int]) -> dict[str, int]:
    while gates:
        remaining_gates = []
        for gate, output in gates:
            result = evaluate_gate(gate, values)
            if result is not None:
                values[output] = result
            else:
                remaining_gates.append((gate, output))
        gates = remaining_gates
    return values

def extract_output(values: dict[str, int]) -> int:
    output_bits = []
    for key in sorted(values.keys()):
        if key.startswith('z'):
            output_bits.append(values[key])
    binary_number = ''.join(map(str, output_bits[::-1]))
    return int(binary_number, 2)

raw_input = open('../inputs/input24.txt').read()
values, gates = parse_input(raw_input)
final_values = simulate(gates, values)
result = extract_output(final_values)
print(result)