from collections import defaultdict, deque

def parse_input(input_text: str) -> tuple[list[tuple[int, int]], list[list[int]]]:
    parts = input_text.strip().split('\n\n')
    rules = [tuple(map(int, rule.split('|'))) for rule in parts[0].split('\n')]
    updates = [list(map(int, update.split(','))) for update in parts[1].split('\n')]
    return rules, updates

def is_update_valid(update: list[int], rules: list[tuple[int, int]]) -> bool:
    page_index = {page: idx for idx, page in enumerate(update)}
    for x, y in rules:
        if x in page_index and y in page_index:
            if page_index[x] >= page_index[y]:
                return False
    return True

def find_middle_page(update: list[int]) -> int:
    mid = len(update) // 2
    return update[mid]

def topological_sort(pages: list[int], rules: list[tuple[int, int]]) -> list[int]:
    graph = defaultdict(list)
    in_degree = {page: 0 for page in pages}

    for x, y in rules:
        if x in pages and y in pages:
            graph[x].append(y)
            in_degree[y] += 1

    queue = deque([page for page in pages if in_degree[page] == 0])
    sorted_pages = []

    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_pages

def solve_puzzle(input_text: str) -> int:
    rules, updates = parse_input(input_text)

    invalid_updates = [update for update in updates if not is_update_valid(update, rules)]
    corrected_updates = [topological_sort(update, rules) for update in invalid_updates]
    middle_pages = [find_middle_page(update) for update in corrected_updates]

    return sum(middle_pages)

input_text = open('../inputs/input5.txt', 'r').read()
print(solve_puzzle(input_text))