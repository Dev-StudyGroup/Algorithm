from collections import deque


def dfs(arr, node, visited):
    print(node, end=' ')
    for n in arr[node]:
        if not visited[n]:
            visited[n] = 1
            dfs(arr, n, visited)


def bfs(arr, node, visited):
    q = deque()
    q.append(node)
    print(node, end=' ')
    visited[node] = 1
    while q:
        now = q.popleft()
        for n in arr[now]:
            if not visited[n]:
                print(n, end=' ')
                visited[n] = 1
                q.append(n)


if __name__ == "__main__":
    N, M, V = map(int, input().split())
    array = [[] for _ in range(N + 1)]
    visited = [0 for _ in range(N + 1)]
    visited[V] = 1
    for _ in range(M):
        a, b = map(int, input().split())
        array[a].append(b)
        array[b].append(a)
    for i in range(1,N+1):
        array[i].sort()
    dfs(array, V, visited)
    print()
    visited = [0 for _ in range(N + 1)]
    bfs(array, V, visited)
