N = int(input())
G = [list(map(int, input().rstrip())) for _ in range(N)]

def dfs(x, y, size):
    if size == 1:
        print(G[x][y], end='')
        return

    num = G[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if num != G[i][j]:
                size //= 2
                print("(", end='')
                dfs(x, y, size)
                dfs(x, y + size, size)
                dfs(x + size, y, size)
                dfs(x + size, y + size, size)
                print(")", end='')
                return

    print(G[x][y], end='')


dfs(0, 0, N)
