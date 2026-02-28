Node = str
Graph = dict[Node, list[Node]]

def parse_input(raw_input: str) -> Graph:
    graph = {}
    lines = raw_input.strip().split('\n')
    for line in lines:
        parts = line.split(':')
        source = parts[0].strip()
        targets = parts[1].strip().split()
        graph[source] = targets
    return graph

def count_paths(start: Node, end: Node, graph: Graph) -> int:
    def dfs(current: Node) -> int:
        if current == end:
            return 1
        if current not in graph:
            return 0

        total_paths = 0
        for neighbor in graph[current]:
            total_paths += dfs(neighbor)
        return total_paths
    return dfs(start)

with open("../inputs/input11.txt", "r") as file:
    data = file.read()
graph = parse_input(data)
print(count_paths("you", "out", graph))