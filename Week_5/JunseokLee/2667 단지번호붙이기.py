import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
input = sys.stdin.readline


def bfs(space, visited, x, y, n):
    q = deque()
    q.append([x, y])
    visited[x][y] = n
    count = 0
    while q:
        a, b = q.pop()
        count += 1
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if space[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = n
                    q.append([nx, ny])
    return count


if __name__ == "__main__":
    N = int(input())
    space = []
    visited = [[0 for _ in range(N)] for _ in range(N)]
    numbers = []
    num = 0
    for _ in range(N):
        space.append(list(map(int, " ".join(input()).rstrip().split())))
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            if space[i][j] == 1:
                num += 1
                numbers.append(bfs(space, visited, i, j, num))
    print(len(numbers))
    numbers.sort()
    for number in numbers:
        print(number)
