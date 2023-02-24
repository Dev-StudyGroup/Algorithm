from collections import deque

N = int(input())
G = [list(map(int, input().rstrip())) for _ in range(N)]
dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]
answer = []
visited = [[False] * N for _ in range(N)]

def in_boundary(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

def bfs(i, j):
    q = deque()
    q.append((i, j))
    cnt = 0
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        cnt += 1
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_boundary(nx, ny) and not visited[nx][ny] and G[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))

    return cnt


for i in range(N):
    for j in range(N):
        if not visited[i][j] and G[i][j] == 1:
            answer.append(bfs(i, j))

answer.sort()
print(len(answer))
for a in answer:
    print(a)
