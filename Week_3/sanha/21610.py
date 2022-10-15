from collections import deque

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
answer = 0
dxs = ['no', 0, -1, -1, -1, 0, 1, 1, 1]
dys = ['no', -1, -1, 0, 1, 1, 1, 0, -1]
clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

def in_boundary(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

for _ in range(M):
    d, s = map(int, input().split())
    visited = [[False] * N for _ in range(N)]
    increased = deque()
    while clouds:
        x, y = clouds.pop()
        nx = (x + dxs[d] * s) % N
        ny = (y + dys[d] * s) % N
        A[nx][ny] += 1
        increased.append((nx, ny))
        visited[nx][ny] = True

    while increased:
        r, c = increased.popleft()
        bucket_cnt = 0
        for i in range(2, 9, 2):
            nr = r + dxs[i]
            nc = c + dys[i]
            if in_boundary(nr, nc) and A[nr][nc] >= 1:
                bucket_cnt += 1
        A[r][c] += bucket_cnt

    for i in range(N):
        for j in range(N):
            if A[i][j] >= 2 and not visited[i][j]:
                clouds.append((i, j))
                A[i][j] -= 2

for i in range(N):
    answer += sum(A[i])
print(answer)
