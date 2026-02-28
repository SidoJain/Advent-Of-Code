from functools import lru_cache

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

def count_paths_between(start: Node, end: Node, graph: Graph) -> int:
    @lru_cache(maxsize=None)
    def dfs(current: Node) -> int:
        if current == end:
            return 1
        if current not in graph:
            return 0

        count = 0
        for neighbor in graph[current]:
            count += dfs(neighbor)
        return count

    if start not in graph:
        return 0
    return dfs(start)

def count_paths(raw_input: str) -> int:
    graph = parse_input(raw_input)
    start_node = 'svr'
    end_node   = 'out'
    mid_a      = 'dac'
    mid_b      = 'fft'

    path_svr_dac = count_paths_between(start_node, mid_a, graph)
    path_dac_fft = count_paths_between(mid_a, mid_b, graph)
    path_fft_out = count_paths_between(mid_b, end_node, graph)
    total_scenario_1 = path_svr_dac * path_dac_fft * path_fft_out

    path_svr_fft = count_paths_between(start_node, mid_b, graph)
    path_fft_dac = count_paths_between(mid_b, mid_a, graph)
    path_dac_out = count_paths_between(mid_a, end_node, graph)
    total_scenario_2 = path_svr_fft * path_fft_dac * path_dac_out

    return total_scenario_1 + total_scenario_2

with open("../inputs/input11.txt", "r") as file:
    data = file.read()
print(count_paths(data))