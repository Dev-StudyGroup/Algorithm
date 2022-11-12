from collections import deque
import sys

#입력
n, m, v = map(int, sys.stdin.readline().rstrip().split())
graph=[[] for i in range(n+1)]
visited=[False]*(n+1)
for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    graph[i].append(j)
    graph[j].append(i)

#중복제거
for i in range(n+1):
    graph[i]=list(set(graph[i]))

#dfs
def dfs(node):
    if visited[node]==False:
        visited[node]=True
        print(node, end=' ')
    graph[node].sort()
    for i in graph[node]:
        if visited[i]==False:
            dfs(i)

#bfs
def bfs(node):
    queue=deque()
    queue.append(node)
    while queue:
        now = queue.popleft()
        
        if visited[now]==False:
            visited[now]=True
            print(now, end=' ')
        
        for i in graph[now]:
            if visited[i]==False:
                queue.append(i)
            
#실행
dfs(v)
visited=[False]*(n+1)
print()
bfs(v)
