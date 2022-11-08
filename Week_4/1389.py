"""
1389: 케빈 베이컨의 6단계 법칙
* 플로이드 워셜
"""
from collections import deque

# N: 유저의 수, M: 친구 관계의 수
N, M = map(int, input().split())
friends = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)

def bacon(graph, start):
    rel = [0] * (N+1)
    queue = deque([start])
    visited[start] = 1
    route = []

    while queue:
        n = queue.popleft()
        for i in graph[n]:
            if visited[i] == 0:
                rel[i] = rel[n] + 1
                queue.append(i)
                visited[i] = 1
                route.append(i)
    return sum(rel)

result = []
for i in range(1, N+1):
    visited = [0 for _ in range(N+1)]
    result.append(bacon(friends,i))

print(result.index(min(result))+1)

