from collections import deque

M, N, H = map(int, input().split())
G = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
answer = -1
dxs = [1, -1, 0, 0, 0, 0]
dys = [0, 0, 1, -1, 0, 0]
dhs = [0, 0, 0, 0, 1, -1]

def check():
    global answer

    for h in range(H):
        for i in range(N):
            for j in range(M):
                if G[h][i][j] == 0:
                    return 0
                answer = max(answer, G[h][i][j])
    return answer

def in_boundary(nh, nx, ny):
    return 0 <= nh < H and 0 <= nx < N and 0 <= ny < M

def bfs(q):
    while q:
        h, x, y = q.popleft()
        for dh, dx, dy in zip(dhs, dxs, dys):
            nh = h + dh
            nx = x + dx
            ny = y + dy
            if in_boundary(nh, nx, ny) and G[nh][nx][ny] == 0:
                G[nh][nx][ny] = G[h][x][y] + 1
                q.append((nh, nx, ny))
    num = check()

    return num - 1

q = deque()
for h in range(H):
    for i in range(N):
        for j in range(M):
            if G[h][i][j] == 1:
                q.append((h, i, j))

print(bfs(q))
