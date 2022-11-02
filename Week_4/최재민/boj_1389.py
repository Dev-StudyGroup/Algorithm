n, m = map(int,input().split())
graph = [[float('inf')]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n+1):
  graph[k][0] = 0
  graph[k][k] = 0
  for i in range(1, n+1):
      for j in range(1, n+1):
          graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

minNum = float('inf')
ans = 0
for i in range(1,n+1):
    tmp = sum(graph[i])
    if minNum > tmp:
        minNum = tmp
        ans = i

print(ans)