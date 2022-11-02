from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        a, b = q.popleft()
        for d in range(4):
            nx, ny = a + dx[d], b + dy[d]
            if 0 <= nx < N and 0 <= ny < M and space[nx][ny] == 1:
                q.append((nx, ny))
                space[nx][ny] = 0


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().split())
        space = [[0 for _ in range(M)] for _ in range(N)]
        count = 0
        for _ in range(K):
            x, y = map(int, input().split())
            space[y][x] = 1
        for i in range(N):
            for j in range(M):
                if space[i][j] == 1:
                    count += 1
                    bfs(i, j)
        print(count)
