from collections import deque

N, M = map(int, input().split())
G = [list(map(int, input().rstrip())) for _ in range(N)]
dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]
INF = int(1e9)
time = [[INF] * M for _ in range(N)]

def in_boundary(nx, ny):
    return 0 <= nx < N and 0 <= ny < M

def bfs(i, j):
    q = deque()
    q.append((i, j))
    time[i][j] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_boundary(nx, ny) and G[nx][ny] == 1 and time[nx][ny] > time[x][y] + 1:
                time[nx][ny] = time[x][y] + 1
                q.append((nx, ny))

bfs(0, 0)
print(time[N - 1][M - 1])
