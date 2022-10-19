from collections import deque
N, K = map(int, input().split())
q = deque([i for i in range(1, N+1)])
result = []
for i in range(N):
    for j in range(K-1):
        q.append(q.popleft())
    result.append(q.popleft())

print("<",end='')
for i in range(len(result)-1):
    print(result[i], end=', ')
print(result[-1],end='')
print(">")