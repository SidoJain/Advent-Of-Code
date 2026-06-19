def parseInput(filename: str) -> tuple[list[str], list[str]]:
    with open(filename) as file:
        workflows, parts = [seg.strip().splitlines() for seg in file.read().split('\n\n')]
    return workflows, parts

def countCombos(workflows: dict[str, list[tuple[str, str, int, str] | tuple[str]]], current_workflow: str, ranges: dict[str, tuple[int, int]]) -> int:
    if current_workflow == 'R':
        return 0
    if current_workflow == 'A':
        product = 1
        for low, high in ranges.values():
            product *= (high - low + 1)
        return product

    total_combinations = 0
    for rule in workflows[current_workflow]:
        if len(rule) == 1:
            target = rule[0]
            total_combinations += countCombos(workflows, target, ranges)
            break
        else:
            category, operator, value, target = rule
            low, high = ranges[category]

            if operator == '>':
                match_range = (max(low, value + 1), high)
                fail_range = (low, min(high, value))
            else:
                match_range = (low, min(high, value - 1))
                fail_range = (max(low, value), high)

            if match_range[0] <= match_range[1]:
                new_ranges = dict(ranges)
                new_ranges[category] = match_range
                total_combinations += countCombos(workflows, target, new_ranges)

            if fail_range[0] <= fail_range[1]:
                ranges = dict(ranges)
                ranges[category] = fail_range
            else:
                break
    return total_combinations

def calcTotalAcceptedCombinations(workflows_data: list[str]) -> int:
    workflows = {}
    for line in workflows_data:
        name, rules_str = line[:-1].split('{')
        rules = rules_str.split(',')
        parsed_rules = []
        for rule in rules:
            if ':' in rule:
                condition, target = rule.split(':')
                category = condition[0]
                operator = condition[1]
                value = int(condition[2:])
                parsed_rules.append((category, operator, value, target))
            else:
                parsed_rules.append((rule,))
        workflows[name] = parsed_rules

    initial_ranges = {
        'x': (1, 4000),
        'm': (1, 4000),
        'a': (1, 4000),
        's': (1, 4000)
    }
    return countCombos(workflows, 'in', initial_ranges)

workflows, parts = parseInput('../inputs/input19.txt')
print(calcTotalAcceptedCombinations(workflows))