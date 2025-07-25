from typing import Callable

def parse_wires(wires_raw: str) -> dict[str, int]:
    wires = {}
    for line in wires_raw.splitlines():
        name, value = line.split(': ')
        wires[name] = int(value)
    return wires

def parse_gates(gates_raw: str, wires: dict[str, int]) -> list[dict[str, str]]:
    gates = []
    for line in gates_raw.splitlines():
        inputs, output = line.split(' -> ')
        a, op, b = inputs.split(' ')
        gates.append({'a': a, 'op': op, 'b': b, 'output': output})
        if a not in wires:
            wires[a] = 0
        if b not in wires:
            wires[b] = 0
        if output not in wires:
            wires[output] = 0
    return gates

def is_direct(gate: dict[str, str]) -> bool:
    return gate['a'].startswith('x') or gate['b'].startswith('x')

def is_output(gate: dict[str, str]) -> bool:
    return gate['output'].startswith('z')

def is_gate(op_type: str) -> Callable:
    return lambda gate: gate['op'] == op_type

def has_output(output: str) -> Callable:
    return lambda gate: gate['output'] == output

def has_input(input: str) -> Callable:
    return lambda gate: gate['a'] == input or gate['b'] == input

def check_FAGate0s(gates: list[dict[str, str]], flags: set[str]) -> list[dict[str, str]]:
    FAGate0s = [gate for gate in gates if is_direct(gate) and gate['op'] == 'XOR']
    for gate in FAGate0s:
        a, b, output = gate['a'], gate['b'], gate['output']

        is_first = a == 'x00' or b == 'x00'
        if is_first:
            if output != 'z00':
                flags.add(output)
            continue
        elif output == 'z00':
            flags.add(output)

        if is_output(gate):
            flags.add(output)
    return FAGate0s

def check_FAGate3s(gates: list[dict[str, str]], flags: set[str]) -> list[dict[str, str]]:
    FAGate3s = [gate for gate in gates if gate['op'] == 'XOR' and not is_direct(gate)]
    for gate in FAGate3s:
        if not is_output(gate):
            flags.add(gate['output'])
    return FAGate3s

def check_output_gates(gates: list[dict[str, str]], flags: set[str], input_bit_count: int) -> None:
    output_gates = [gate for gate in gates if is_output(gate)]
    for gate in output_gates:
        is_last = gate['output'] == f'z{input_bit_count:03d}'
        if is_last:
            if gate['op'] != 'OR':
                flags.add(gate['output'])
            continue
        elif gate['op'] != 'XOR':
            flags.add(gate['output'])

def check_check_next(FAGate0s: list[dict[str, str]], FAGate3s: list[dict[str, str]], flags: set[str]) -> list[dict[str, str]]:
    check_next = []
    for gate in FAGate0s:
        output = gate['output']

        if output in flags:
            continue
        if output == 'z00':
            continue

        matches = [g for g in FAGate3s if has_input(output)(g)]
        if len(matches) == 0:
            check_next.append(gate)
            flags.add(output)
    return check_next

def check_flags_for_check_next(gates: list[dict[str, str]], check_next: list[dict[str, str]], FAGate3s: list[dict[str, str]], flags: set[str]) -> None:
    for gate in check_next:
        a = gate['a']
        intended_result = f'z{a[1:]}'
        matches = [g for g in FAGate3s if has_output(intended_result)(g)]

        match = matches[0]
        to_check = [match['a'], match['b']]
        or_matches = [g for g in gates if g['op'] == 'OR' and g['output'] in to_check]

        or_match_output = or_matches[0]['output']
        correct_output = next(output for output in to_check if output != or_match_output)
        flags.add(correct_output)

data = open('../inputs/input24.txt').read().split('\n\n')
wires_raw, gates_raw = data
wires = parse_wires(wires_raw)
gates = parse_gates(gates_raw, wires)

input_bit_count = len(wires_raw.splitlines()) // 2
flags = set()

FAGate0s = check_FAGate0s(gates, flags)
FAGate3s = check_FAGate3s(gates, flags)
check_output_gates(gates, flags, input_bit_count)
check_next = check_check_next(FAGate0s, FAGate3s, flags)
check_flags_for_check_next(gates, check_next, FAGate3s, flags)

flags_arr = sorted(flags)[:-1]
print(','.join(flags_arr))