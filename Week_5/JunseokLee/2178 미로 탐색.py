from collections import deque
import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
input = sys.stdin.readline 
res = int(1e9)


def bfs(x, y, array):
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        if x == N - 1 and y == M - 1:
            return array[x][y]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
            if space[nx][ny] and not array[nx][ny]:
                array[nx][ny] = array[x][y] + 1
                q.append([nx, ny])


if __name__ == "__main__":
    N, M = map(int, input().split())
    space = []
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    for _ in range(N):
        space.append(list(map(int, ' '.join(input()).split())))
    print(bfs(0, 0, visited))
