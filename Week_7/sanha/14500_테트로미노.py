N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
answer = -1
dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]
visited = [[False] * M for _ in range(N)]

def in_boundary(nx, ny):
    return 0 <= nx < N and 0 <= ny < M

def dfs(x, y, total, depth):
    global answer

    if depth == 4:
        answer = max(answer, total)
        return

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_boundary(nx, ny) and not visited[nx][ny]:
            if depth == 2:
                visited[nx][ny] = True
                dfs(x, y, total + G[nx][ny], depth + 1)
                visited[nx][ny] = False
            visited[nx][ny] = True
            dfs(nx, ny, total + G[nx][ny], depth + 1)
            visited[nx][ny] = False

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = True
            dfs(i, j, G[i][j], 1)
            visited[i][j] = False

print(answer)
