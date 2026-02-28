import re

def solve_claw_machine(button_a_x: int, button_a_y: int, button_b_x: int, button_b_y: int, final_x: int, final_y: int) -> int:
    final_x += 10000000000000
    final_y += 10000000000000

    i_value = (final_x * button_b_y - final_y * button_b_x) / (button_a_x * button_b_y - button_a_y * button_b_x)
    j_value = (final_y * button_a_x - final_x * button_a_y) / (button_a_x * button_b_y - button_a_y * button_b_x)
    if i_value == int(i_value) and j_value == int(j_value):
        return 3 * int(i_value) + int(j_value)

    return 0

with open('../inputs/input13.txt') as file:
    raw_data = file.read().split('\n\n')

pattern = r'[+-=]?(\d+)'
machines = []
for machine in raw_data:
    match = re.findall(pattern, machine)
    machines.append(list(map(int, match)))

result = 0
for machine in machines:
    result += solve_claw_machine(*machine)

print(result)