import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
        return
    parent[a] = b


if __name__ == "__main__":
    N, M = map(int, input().split())
    parent = [0] * (N + 1)
    graph_set = set()
    for i in range(1, N + 1):
        parent[i] = i

    for _ in range(M):
        u, v = map(int, input().split())
        union_parent(parent, u, v)

    for i in range(1, N + 1):
        parent[i] = find_parent(parent, i)

    for i in range(1, N + 1):
        graph_set.add(parent[i])

    print(len(graph_set))
