from itertools import product

def readFile(filename: str) -> str:
    with open(filename, 'r') as f:
        return f.read()

def evalExpression(numbers: list[int], operators: tuple[str, ...]) -> int:
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif operators[i] == '|':
            result = int(str(result) + str(numbers[i + 1]))
    return result

def parseInput(data: str) -> list[tuple[int, list[int]]]:
    equations = []
    for line in data.strip().split('\n'):
        value, numbers = line.split(':')
        value = int(value.strip())
        numbers = list(map(int, numbers.split()))
        equations.append([value, numbers])
    return equations

def calcResult(data: str) -> int:
    equations = parseInput(data)
    result = 0

    for value, numbers in equations:
        num_operators = len(numbers) - 1
        possible_operators = product('+|*', repeat=num_operators)

        for operators in possible_operators:
            if evalExpression(numbers, operators) == value:
                result += value
                break

    return result

input_data = readFile('../inputs/input7.txt')
result = calcResult(input_data)
print(result)