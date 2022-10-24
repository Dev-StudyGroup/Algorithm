"""
1260: DFS와 BFS

DFS: 깊이 우선 탐색 -> 스택 사용
BFS: 너비 우선 탐색 -> 큐 사용
"""
from collections import deque

def dfs(graph, v):
    visited = []
    stack = [v]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse = True) # stack은 LIFO이므로 내림차순 정렬
                stack += temp

    return " ".join(str(i) for i in visited)

def bfs(graph, v):
    visited = []
    queue = deque([v])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                queue += temp

    return " ".join(str(i) for i in visited)

# N: 정점의 개수, M: 간선의 개수, V: 탐색을 시작할 정점의 번호 
N, M, V = map(int,input().split())

graph = {}
for i in range(M):
    start, end = map(int,input().split())
    if start not in graph:
        graph[start] = [end]
    elif end not in graph[start]:
        graph[start].append(end)

    if end not in graph:
        graph[end] = [start]
    elif start not in graph[end]:
        graph[end].append(start)

print(dfs(graph, V))
print(bfs(graph, V))