from collections import deque

N, K = map(int, input().split())
q = deque([i for i in range(1, N + 1)])
answer = []

while q:
    q.rotate(-(K - 1))
    answer.append(q.popleft())

print("<", end='')
for i in range(len(answer) - 1):
    print("%d, " %answer[i], end='')
print(answer[-1], end='')
print(">")
