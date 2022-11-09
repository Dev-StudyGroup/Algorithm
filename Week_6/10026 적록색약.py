from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs1(a, b, visited):
    q = deque()
    q.append([a, b])
    visited[a][b] = 1

    while q:
        x, y = q.popleft()
        now = space[x][y]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if space[nx][ny] == now:
                    visited[nx][ny] = 1
                    q.append([nx, ny])


def bfs2(a, b, visited):
    q = deque()
    q.append([a, b])
    visited[a][b] = 1

    while q:
        x, y = q.popleft()
        now = space[x][y]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if now == 'B':
                    if space[nx][ny] == now:
                        visited[nx][ny] = 1
                        q.append([nx, ny])
                else:
                    if space[nx][ny] != 'B':
                        visited[nx][ny] = 1
                        q.append([nx, ny])


if __name__ == "__main__":
    N = int(input())
    space = []
    for _ in range(N):
        space.append(" ".join(input().split()))
    visited1 = [[0 for _ in range(N)] for _ in range(N)]
    visited2 = [[0 for _ in range(N)] for _ in range(N)]
    result1, result2 = 0, 0

    for i in range(N):
        for j in range(N):
            if not visited1[i][j]:
                result1 += 1
                bfs1(i, j, visited1)

    for i in range(N):
        for j in range(N):
            if not visited2[i][j]:
                result2 += 1
                bfs2(i, j, visited2)

    print(result1, result2)
