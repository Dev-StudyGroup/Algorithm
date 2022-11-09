import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][k] + graph[k][j] >= 2:
                    graph[i][j] = 1

    for i in range(N):
        for j in range(N):
            print(graph[i][j], end=' ')
        print()
