"""
1012: 유기농 배추
"""
import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    visited[x][y] = 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]  
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if board[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)

t = int(input())

for _ in range(t):    
    m, n, k = map(int, input().split())
    #worm = k
    board = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for c in range(k):
        y, x = map(int, input().split())
        board[x][y] = 1

    worm = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] and not visited[i][j]:
                dfs(i,j)
                worm += 1
    print(worm)

