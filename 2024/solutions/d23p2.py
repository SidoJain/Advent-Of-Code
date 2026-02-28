from collections import defaultdict

def parse_input(data: str) -> defaultdict[str, set[str]]:
    graph = defaultdict(set)
    for line in data.strip().split('\n'):
        a, b = line.split('-')
        graph[a].add(b)
        graph[b].add(a)
    return graph

def find_cluster(graph: defaultdict[str, set[str]], cluster: set[str], candidates: set, exculded: set, clusters: list[set[str]]) -> None:
    if not candidates and not exculded:
        clusters.append(cluster)
        return
    for node in list(candidates):
        neighbors = graph[node]
        find_cluster(graph, cluster | {node}, candidates & neighbors, exculded & neighbors, clusters)
        candidates.remove(node)
        exculded.add(node)

def find_largest_cluster(graph: defaultdict[str, set[str]]) -> list[str]:
    clusters = []
    find_cluster(graph, set(), set(graph.keys()), set(), clusters)
    largest_cluster = max(clusters, key=len)
    return sorted(largest_cluster)

data = open('../inputs/input23.txt').read()
graph = parse_input(data)
largest_cluster = find_largest_cluster(graph)
password = ','.join(largest_cluster)
print(password)