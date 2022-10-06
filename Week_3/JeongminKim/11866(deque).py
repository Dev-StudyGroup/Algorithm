
"""
    2번째 방식
"""
from collections import deque

N, k = map(int, input().split())
table = deque()
for i in range(1, N + 1):
    table.append(i)
out = []
while table:
    for _ in range(k - 1):
        table.append(table.popleft())
    out.append(table.popleft())

print('<', end='')
for i in range(len(out) - 1):
    print(f'{out[i]}, ', end='')
print(out[-1], end='')
print('>')