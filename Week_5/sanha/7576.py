from collections import deque

M, N = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]
q = deque()
INF = int(1e9)
answer = -2

def in_boundary(nx, ny):
    return 0 <= nx < N and 0 <= ny < M

def check():
    global answer

    for i in range(N):
        for j in range(M):
            if G[i][j] == 0:
                return 0
            answer = max(answer, G[i][j])

    return answer

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_boundary(nx, ny) and G[nx][ny] == 0:
                G[nx][ny] = G[x][y] + 1
                q.append((nx, ny))
    num = check()
    return num - 1


for i in range(N):
    for j in range(M):
        if G[i][j] == 1:
            q.append((i, j))

print(bfs())
