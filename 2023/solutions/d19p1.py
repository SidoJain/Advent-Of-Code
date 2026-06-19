def parseInput(filename: str) -> tuple[list[str], list[str]]:
    with open(filename) as file:
        workflows, parts = [seg.strip().splitlines() for seg in file.read().split('\n\n')]
    return workflows, parts

def calcSumOfAcceptedParts(workflows_data: list[str], parts_data: list[str]) -> int:
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

    total_accepted_sum = 0
    for line in parts_data:
        part = {}
        for item in line[1:-1].split(','):
            cat, val = item.split('=')
            part[cat] = int(val)

        current_workflow = 'in'
        while current_workflow not in ('A', 'R'):
            for rule in workflows[current_workflow]:
                if len(rule) == 1:
                    current_workflow = rule[0]
                    break
                else:
                    category, operator, value, target = rule
                    part_value = part[category]
                    if operator == '>':
                        if part_value > value:
                            current_workflow = target
                            break
                    elif operator == '<':
                        if part_value < value:
                            current_workflow = target
                            break
        if current_workflow == 'A':
            total_accepted_sum += sum(part.values())
    return total_accepted_sum

workflows, parts = parseInput('../inputs/input19.txt')
print(calcSumOfAcceptedParts(workflows, parts))