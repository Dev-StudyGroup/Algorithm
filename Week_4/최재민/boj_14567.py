import sys
from collections import deque
from collections import defaultdict
n, m = map(int, input().split())

indegree = [0]*(n+1)
answer = [0]*(n+1)
graph = defaultdict(list)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    indegree[b] += 1
    graph[a].append(b)

dq = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        dq.append(i)
        answer[i] = 1

while dq:
    now = dq.popleft()
    for i in graph[now]:
        indegree[i] -= 1
        answer[i] = answer[now] + 1
        if indegree[i] == 0:
            dq.append(i)

print(*answer[1:])  # *쓰면 인자를 여러개준 효과를 냄