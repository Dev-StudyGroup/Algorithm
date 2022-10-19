"""
요세푸스 문제 0
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
from collections import deque

n, k = map(int, input().split())
queue = deque(list(x for x in range(1, n + 1)))
result = []

while queue:
    for i in range(k - 1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print('<', end="")
for i in range(n):
    if i == n - 1:
        print(result[i], end="")
    else:
        print(result[i], end=", ")
print('>')
