from collections import deque
T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if 0<= nx< N and 0<= ny< M and highland[nx][ny] == 1:
                highland[nx][ny] = 0
                queue.append([nx, ny])


for _ in range(T):
    M, N, K = map(int, input().split())
    highland = [[0] * M for i in range(N)]
    cnt = 0

    for i in range(K):
        a, b = map(int, input().split())
        highland[b][a] = 1

    for i in range(N):
        for j in range(M):
            if highland[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)


