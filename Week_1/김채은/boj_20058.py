# [BOJ] 20058 마법사 상어와 파이어스톰
# PyPy3 통과

from collections import deque
from copy import deepcopy

global n
n, q = map(int, input().split())
n = 2 ** n

board = [list(map(int, input().split())) for _ in range(n)]
step = list(map(int, input().split()))

def firestorm(l):
    global n
    nboard = [[0]*n for _ in range(n)]
    leng = 2**l
    for i in range(0, n, leng):
        for j in range(0, n, leng):
            nboard = rotate(nboard, i, j, leng)

    nboard = fire(nboard)
    
    return nboard

def rotate(nboard, y, x, leng):
    for i, b in zip(range(y, y + leng), range(x, x + leng)):
        for j, a in zip(range(x, x + leng), range(y + leng - 1, y - 1, -1)):
            nboard[i][j] = board[a][b]

    return nboard

def fire(nboard):
    cboard = deepcopy(nboard)

    dys, dxs = [0, 1, 0, -1], [1, 0, -1, 0]

    for i in range(n):
        for j in range(n):
            
            if not nboard[i][j]:
                continue

            ice = 0
            
            for dy, dx in zip(dys, dxs):
                ny, nx = i + dy, j + dx

                if in_range(ny, nx) and nboard[ny][nx]:
                    ice += 1
            if cboard[i][j] and ice < 3:
                cboard[i][j] -= 1

    return cboard

def bfs(i, j):
    dys, dxs = [0, 1, 0, -1], [1, 0, -1, 0]

    dq = deque([(i,j)])
    count = 0

    while dq:
        y, x = dq.popleft()
        
        for dy, dx in zip(dys, dxs):
            ny, nx = y+dy,x+dx
            if in_range(ny, nx) and not visited[ny][nx] and board[ny][nx]:
                dq.append((ny,nx))
                visited[ny][nx] = True
                count += 1

    return count

def in_range(y, x):
    global n
    if 0 <= y < n and 0 <= x < n:
        return True
    return False

for st in step:
    board = firestorm(st)



ans_sum = 0
ans_count = 0
visited = [[False]*(n) for _ in range(n)]

for i in range(n):
    for j in range(n):
        ans_sum += board[i][j]

        if not visited[i][j] and board[i][j]:
            count = bfs(i,j)
            ans_count = max(ans_count, count)

print(ans_sum)
print(ans_count)
