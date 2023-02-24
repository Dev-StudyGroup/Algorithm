"""

    DFS, BFS로 탐색한 결과를 출력

"""
from collections import defaultdict


def DFS(g, n_nodes, v):
    route = []
    stack = [v]
    visited = [0] * (n_nodes + 1)
    while stack:
        cur_node = stack.pop(-1)
        if visited[cur_node] == 0:
            visited[cur_node] = 1
            route.append(cur_node)
        for next_node in sorted(g[cur_node], reverse=True):
            if not visited[next_node]:
                stack.append(next_node)

    return ' '.join(map(str, route))


def BFS(g, n_nodes, v):
    queue = [v]
    visited = [0] * (n_nodes + 1)
    route = []
    while queue:
        cur_node = queue.pop(0)
        if not visited[cur_node]:
            visited[cur_node] = 1
            route.append(cur_node)

        for next_node in g[cur_node]:
            if not visited[next_node]:
                queue.append(next_node)

    return ' '.join(map(str, route))


if __name__ == '__main__':
    N, M, V = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    for key in graph.keys():
        graph[key] = sorted(graph[key])
    print(DFS(graph, N, V))
    print(BFS(graph, N, V))
