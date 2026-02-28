import numpy as np
from scipy.optimize import linprog

def min_presses_for_joltage(line: str) -> int:
    _, *buttons, counters = line.split(" ")
    goal = tuple(map(int, counters[1:-1].split(",")))
    moves = []
    for button in buttons:
        button = button[1:-1]
        button = {int(x) for x in button.split(",")}
        moves.append(button)

    coef = [1 for _ in moves]
    A_eq = []
    b_eq = []
    for i in range(len(goal)):
        A_eq.append([1 if i in move else 0 for move in moves])
        b_eq.append(goal[i])
    A_eq = np.array(A_eq)
    b_eq = np.array(b_eq)
    res = linprog(c=coef, A_eq=A_eq, b_eq=b_eq, integrality=True)
    return int(res.fun)

with open("../inputs/input10.txt") as file:
    data = [line.strip() for line in file.readlines()]
print(sum(min_presses_for_joltage(line) for line in data))