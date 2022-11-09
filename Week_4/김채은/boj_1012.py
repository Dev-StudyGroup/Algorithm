from typing import Final
from collections import deque

def in_range(y, x):
    return 0 <= y < n and 0 <= x < m

def findCabbageGroup(y, x):
    global visited

    dq = deque([(y, x)])

    dys, dxs = [1, 0, -1, 0], [0, 1, 0, -1]

    while dq:
        i, j = dq.popleft()

        for dy, dx in zip(dys, dxs):
            ny, nx = i + dy, j + dx

            if in_range(ny, nx) and not visited[ny][nx]:
                if matrix[ny][nx] == CABBAGE:
                    dq.append((ny, nx))

                visited[ny][nx] = True

    
if __name__ == "__main__":
    t = int(input())

    EMPTY: Final = 0
    CABBAGE: Final = 1

    for _ in range(t):
        m, n, k = map(int, input().split())

        matrix = [[EMPTY for _ in range(m)] for _ in range(n)]

        for __ in range(k):
            x, y = map(int, input().split())

            matrix[y][x] = CABBAGE

        global visited
        visited = [[False for _ in range(m)] for _ in range(n)]

        cabbageGroup = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == CABBAGE and not visited[i][j]:
                    findCabbageGroup(i, j)

                    cabbageGroup += 1

        print(cabbageGroup)