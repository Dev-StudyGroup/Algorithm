from collections import deque
from copy import deepcopy

N, Q = map(int, input().split())
NN = 2 ** N
G = [list(map(int, input().split())) for _ in range(NN)]
fire_balls = list(map(int, input().split()))
dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]
total, Max = 0, 0

def in_boundary(nx, ny):
    return 0 <= nx < NN and 0 <= ny < NN

def rotate(L):
    k = 2 ** L
    tmp = deepcopy(G)
    for x in range(0, NN, k):
        for y in range(0, NN, k):
            for i in range(k):
                for j in range(k):
                    G[x + j][y + k - i - 1] = tmp[x + i][y + j]

def melt():
    global G
    tmp = deepcopy(G)
    for x in range(NN):
        for y in range(NN):
            if G[x][y] != 0:
                cnt = 0
                for dx, dy in zip(dxs, dys):
                    nx = x + dx
                    ny = y + dy
                    if in_boundary(nx, ny):
                        if G[nx][ny] != 0:
                            cnt += 1
                if cnt < 3:
                    tmp[x][y] -= 1
    G = deepcopy(tmp)

def find_total_max():
    global total, Max
    for i in range(NN):
        for j in range(NN):
            if G[i][j] != 0:
                q = deque()
                q.append((i, j))
                total += G[i][j]
                G[i][j] = 0
                cnt = 0
                while q:
                    x, y = q.popleft()
                    cnt += 1
                    for dx, dy in zip(dxs, dys):
                        nx = x + dx
                        ny = y + dy
                        if in_boundary(nx, ny) and G[nx][ny] != 0:
                            total += G[nx][ny]
                            q.append((nx, ny))
                            G[nx][ny] = 0
                Max = max(Max, cnt)

for L in fire_balls:
    rotate(L)
    melt()
find_total_max()
print(total)
print(Max)
