from collections import deque

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
sx, sy = 0, 0
ate, body_size = 0, 2
dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]
answer = 0

for i in range(N):
    for j in range(N):
        if G[i][j] == 9:
            sx, sy = i, j
            G[i][j] = 0

def in_boundary(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

def bfs():
    distance = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    tmp = []
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_boundary(nx, ny) and not visited[nx][ny]:
                if G[nx][ny] <= body_size:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    distance[nx][ny] = distance[x][y] + 1
                    if G[nx][ny] != 0 and G[nx][ny] < body_size:
                        tmp.append((distance[nx][ny], nx, ny))
    tmp.sort(key=lambda x: (-x[0], -x[1], -x[2]))
    return tmp

while True:
    shark = bfs()
    if len(shark) == 0:
        break
    distance, nx, ny = shark.pop()
    answer += distance
    sx, sy = nx, ny
    G[nx][ny] = 0

    ate += 1
    if ate == body_size:
        body_size += 1
        ate = 0

print(answer)
