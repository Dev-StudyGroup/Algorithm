N,M,V=map(int,input().split())
s=[[0]*(N+1) for i in range(N+1)]
visit = [0 for i in range(N+1)]

for i in range(M):
    x,y = map(int,input().split())
    s[x][y] = 1
    s[y][x] = 1

def dfs(V):
    print(V, end=' ')
    visit[V] = 1
    for i in range(1,N+1):
        if visit[i] == 0 and s[V][i] == 1:
            dfs(i)

def bfs(v):
    queue = [v]
    visit[v] = 0
    while(queue):
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1, N + 1):
            if visit[i] == 1 and s[v][i] == 1:
                queue.append(i)
                visit[i] = 0

dfs(V)
print()
bfs(V)