from collections import deque, defaultdict

def parseInput(filename: str) -> defaultdict[str, list[str]]:
    graph = defaultdict(list)
    with open(filename) as file:
        for line in file:
            left, rights = line.strip().split(": ")
            for right in rights.split():
                graph[left].append(right)
                graph[right].append(left)
    return graph

def reduceConnectionLoad(graph: defaultdict[str, list[str]]) -> int:
    nodes = list(graph.keys())
    source = nodes[0]
    for sink in nodes[1:]:
        flow = defaultdict(int)

        def bfs():
            queue = deque([source])
            parent = {source: None}
            while queue:
                cur = queue.popleft()
                if cur == sink:
                    break

                for nxt in graph[cur]:
                    if nxt not in parent and (1 - flow[(cur, nxt)]) > 0:
                        parent[nxt] = cur
                        queue.append(nxt)
            if sink not in parent:
                return None

            path = []
            cur = sink
            while cur != source:
                prev = parent[cur]
                path.append((prev, cur))
                cur = prev
            return path

        max_flow = 0
        while True:
            path = bfs()
            if not path:
                break

            max_flow += 1
            if max_flow > 3:
                break
            for u, v in path:
                flow[(u, v)] += 1
                flow[(v, u)] -= 1

        if max_flow == 3:
            reachable = {source}
            queue = deque([source])
            while queue:
                cur = queue.popleft()
                for nxt in graph[cur]:
                    if nxt not in reachable and (1 - flow[(cur, nxt)]) > 0:
                        reachable.add(nxt)
                        queue.append(nxt)

            group1_size = len(reachable)
            group2_size = len(nodes) - group1_size
            return group1_size * group2_size

graph = parseInput('../inputs/input25.txt')
print(reduceConnectionLoad(graph))