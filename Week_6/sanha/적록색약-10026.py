from collections import deque

N = int(input())
M = [list(map(str, input())) for _ in range(N)]
dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]
visited = [[False] * N for _ in range(N)]

partA, partB = 0, 0

def change_colour():
    for i in range(N):
        for j in range(N):
            if M[i][j] == 'G':
                M[i][j] = 'R'

def in_boundary(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

def bfs(i, j, colour):
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_boundary(nx, ny) and not visited[nx][ny] and M[nx][ny] == colour:
                visited[nx][ny] = True
                q.append((nx, ny))

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, M[i][j])
            partA += 1

change_colour()
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, M[i][j])
            partB += 1

print(partA, partB)
