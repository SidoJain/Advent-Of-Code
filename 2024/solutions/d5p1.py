def readFile(filename: str) -> str:
    with open(filename) as f:
        return f.read()

def parse_input(input_text: str) -> tuple[list[tuple[int, int]], list[list[int]]]:
    parts = input_text.strip().split('\n\n')
    rules = [tuple(map(int, rule.split('|'))) for rule in parts[0].split('\n')]
    updates = [list(map(int, update.split(','))) for update in parts[1].split('\n')]
    return rules, updates

def is_update_valid(update: list[list[int]], rules: list[tuple[int, int]]) -> bool:
    page_index = {page: idx for idx, page in enumerate(update)}
    for x, y in rules:
        if x in page_index and y in page_index:
            if page_index[x] >= page_index[y]:
                return False
    return True

def find_middle_page(update: list[int]) -> int:
    mid = len(update) // 2
    return update[mid]

def solve_puzzle(input_text: str) -> int:
    rules, updates = parse_input(input_text)
    valid_updates = [update for update in updates if is_update_valid(update, rules)]
    middle_pages = [find_middle_page(update) for update in valid_updates]
    return sum(middle_pages)

input_text = readFile('../inputs/input5.txt')
print(solve_puzzle(input_text))