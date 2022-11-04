import sys
from collections import deque

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
input = sys.stdin.readline


def bfs(q, tomatoes):
    while q:
        z, y, x = q.popleft()
        for d in range(6):
            nz = z + dz[d]
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and tomatoes[nz][ny][nx] == 0:
                tomatoes[nz][ny][nx] = tomatoes[z][y][x] + 1
                q.append([nz, ny, nx])


if __name__ == "__main__":
    M, N, H = map(int, input().split())
    tomatoes = []
    q = deque()
    flag = False
    for h in range(H):
        tomato = []
        for n in range(N):
            arr = list(map(int, input().split()))
            tomato.append(arr)
            for m in range(len(arr)):
                if arr[m] == 1:
                    q.append([h, n, m])
        tomatoes.append(tomato)
    bfs(q, tomatoes)
    result = -1
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomatoes[h][n][m] == 0:
                    flag = True
            result = max(result, max(tomatoes[h][n]))
    if flag:
        print(-1)
    else:
        print(result - 1)
