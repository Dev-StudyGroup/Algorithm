import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(space, q):
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and space[nx][ny] == 0:
                space[nx][ny] = space[x][y] + 1
                q.append([nx, ny])


if __name__ == "__main__":
    M, N = map(int, input().split())
    space = []
    q = deque()
    result = -1
    flag = False

    for n in range(N):
        arr = list(map(int, input().split()))
        space.append(arr)
        for m in range(len(arr)):
            if arr[m] == 1:
                q.append([n, m])

    bfs(space, q)

    for i in range(N):
        for j in range(M):
            if space[i][j] == 0:
                flag = True
            result = max(result, space[i][j])

    if flag:
        print(-1)
    else:
        print(result - 1)
