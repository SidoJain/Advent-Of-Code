from collections import defaultdict

def parse_input(data: str) -> defaultdict[str, set[str]]:
    graph = defaultdict(set)
    for line in data.strip().split('\n'):
        a, b = line.split('-')
        graph[a].add(b)
        graph[b].add(a)
    return graph

def find_triads(graph: defaultdict[str, set[str]]) -> set[str]:
    triads = set()
    for node in graph:
        neighbors = graph[node]
        for neighbor in neighbors:
            for mutual in neighbors.intersection(graph[neighbor]):
                triad = tuple(sorted([node, neighbor, mutual]))
                triads.add(triad)
    return triads

def count_triads_with_t(triads: set[str]) -> int:
    return sum(1 for triad in triads if any(comp.startswith('t') for comp in triad))

data = open('../inputs/input23.txt').read()
graph = parse_input(data)
triads = find_triads(graph)
result = count_triads_with_t(triads)
print(result)