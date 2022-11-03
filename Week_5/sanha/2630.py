N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
blues, whites = 0, 0

def dfs(x, y, size):
    global whites, blues

    if size == 1:
        if not visited[x][y]:
            visited[x][y] = True
            if G[x][y] == 0:
                whites += 1
            else:
                blues += 1
        return

    num = G[x][y]
    flag = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if G[i][j] != num or visited[i][j]:
                flag = False
                break

    if flag:
        for i in range(x, x + size):
            for j in range(y, y + size):
                visited[i][j] = True

        if num == 0:
            whites += 1
        else:
            blues += 1
    else:
        size //= 2
        dfs(x, y, size)
        dfs(x, y + size, size)
        dfs(x + size, y, size)
        dfs(x + size, y + size, size)

dfs(0, 0, N)
print(whites)
print(blues)
