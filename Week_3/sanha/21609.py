from collections import deque

N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]
answer = 0

def in_boundary(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

def bfs(x, y, colour):
    block_cnt = 1
    rainbow_cnt = 0
    blocks = [(x, y)]
    rainbows = []
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_boundary(nx, ny) and not visited[nx][ny] and G[nx][ny] > -1:
                if G[nx][ny] == 0:
                    block_cnt += 1
                    rainbow_cnt += 1
                    rainbows.append((nx, ny))
                    q.append((nx, ny))
                    visited[nx][ny] = True
                if G[nx][ny] == colour:
                    block_cnt += 1
                    blocks.append((nx, ny))
                    q.append((nx, ny))
                    visited[nx][ny] = True

    for i, j in rainbows:
        visited[i][j] = False

    return (block_cnt, rainbow_cnt, blocks + rainbows)

def remove(tmp):
    for i, j in tmp:
        G[i][j] = -2

def rotate(G):
    return list(map(list, zip(*G)))[::-1]

def gravity():
    for j in range(N):
        for i in range(N - 2, -1, -1):
            if G[i][j] > -1:
                r = i
                while r + 1 < N and G[r + 1][j] == -2:
                    G[r + 1][j] = G[r][j]
                    G[r][j] = -2
                    r += 1


while True:
    visited = [[False] * N for _ in range(N)]
    groups = []
    for x in range(N):
        for y in range(N):
            if G[x][y] > 0 and not visited[x][y]:
                colour = G[x][y]
                block = bfs(x, y, colour)
                if block[0] >= 2:
                    groups.append(block)

    if not groups:
        break

    groups.sort(reverse=True)
    answer += groups[0][0] ** 2
    remove(groups[0][2])
    gravity()
    G = rotate(G)
    gravity()

print(answer)
