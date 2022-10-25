if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[int(1e9) for _ in range(N)] for _ in range(N)]
    res = -1
    kevin_bacon = int(1e9)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a-1][b-1] = 1
        graph[b-1][a-1] = 1

    for i in range(N):
        graph[i][i] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(N):
        if kevin_bacon > sum(graph[i]):
            kevin_bacon = sum(graph[i])
            res = i+1
    print(res)