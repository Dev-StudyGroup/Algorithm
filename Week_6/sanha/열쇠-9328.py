from collections import deque
from collections import defaultdict

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]
tc = int(input())

def new_G():
    for i in G:
        i.insert(0, '.')
        i.append('.')
    G.insert(0, ['.'] * (w + 2))
    G.append(['.'] * (w + 2))

def in_boundary(nx, ny):
    return 0 <= nx < h + 2 and 0 <= ny < w + 2

def bfs(a, b):
    cnt = 0
    q = deque()
    q.append([a, b])
    visited = [[False] * (w + 2) for _ in range(h + 2)]
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_boundary(nx, ny) and G[nx][ny] != '*' and not visited[nx][ny]:
                if G[nx][ny] == '.':
                    q.append((nx, ny))
                    visited[nx][ny] = True
                elif G[nx][ny] == '$':
                    cnt += 1
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    G[nx][ny] = '.'
                elif G[nx][ny].isalpha() and G[nx][ny].isupper():
                    if key_dic[G[nx][ny].lower()]:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        G[nx][ny] = '.'
                elif G[nx][ny].isalpha() and G[nx][ny].islower():
                    q = deque()
                    visited = [[False] * (w + 2) for _ in range(h + 2)]
                    key_dic[G[nx][ny]] = True
                    G[nx][ny] = '.'
                    q.append((nx, ny))

    return cnt

for _ in range(tc):
    h, w = map(int, input().split())
    G = [list(map(str, input())) for _ in range(h)]
    keys = list(map(str, input()))
    key_dic = defaultdict(bool)

    for i in range(65, 91):
        key_dic[chr(i)] = False
    for key in keys:
        key_dic[key] = True

    new_G()
    print(bfs(0, 0))
