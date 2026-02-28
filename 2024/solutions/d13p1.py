def read_file(file_path: str) -> list[tuple[int, int, int, int, int, int]]:
    with open(file_path, 'r') as file:
        machines = []
        for machine in file.read().split('\n\n'):
            temp = []
            for line in machine.split('\n'):
                for inp in line.split(':')[1:]:
                    for i in inp.split(', '):
                        i = i.strip()
                        try:
                            temp.append(i.split('+')[1])
                        except:
                            temp.append(i.split('=')[1])
            machines.append(tuple(map(int, temp)))

    return machines

def solve_claw_machine(machines: list[tuple[int, int, int, int, int, int]]) -> tuple[int, float]:
    total_tokens = 0
    prizes_won = 0

    for machine in machines:
        A_x, A_y, B_x, B_y, P_x, P_y = machine
        min_cost = float('inf')
        found_solution = False

        for a in range(101):
            for b in range(101):
                if (a * A_x + b * B_x == P_x) and (a * A_y + b * B_y == P_y):
                    cost = 3 * a + b
                    if cost < min_cost:
                        min_cost = cost
                        found_solution = True

        if found_solution:
            prizes_won += 1
            total_tokens += min_cost

    return prizes_won, total_tokens

machines = read_file('../inputs/input13.txt')
prizes, tokens = solve_claw_machine(machines)
print(f'Prizes won: {prizes}, Total tokens spent: {tokens}')