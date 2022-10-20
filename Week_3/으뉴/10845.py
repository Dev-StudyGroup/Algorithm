import sys
from collections import deque
input = sys.stdin.readline

q = deque()
orders = [input().rstrip() for _ in range(int(input()))]

for order in orders:
    if 'push' in order:
        q.append(order.split()[1])
    elif 'pop' in order:
        print(q.pop() if q else -1)
    elif 'size' in order:
        print(len(q))
    elif 'empty' in order:
        print(0 if q else 1)
    elif 'front' in order:
        print(q[0] if q else -1)
    elif 'back' in order:
        print(q[-1] if q else -1)
