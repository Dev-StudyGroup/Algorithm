import sys
from collections import deque
input = sys.stdin.readline

dq = deque()
orders = [input().rstrip() for _ in range(int(input()))]

for order in orders:
    if 'push_front' in order:
        dq.appendleft(order.split()[1])
    elif 'push_back' in order:
        dq.append(order.split()[1])
    elif 'pop_front' in order:
        print(dq.popleft() if dq else -1)
    elif 'pop_back' in order:
        print(dq.pop() if dq else -1)
    elif 'size' in order:
        print(len(dq))
    elif 'empty' in order:
        print(0 if dq else 1)
    elif 'front' in order:
        print(dq[0] if dq else -1)
    elif 'back' in order:
        print(dq[-1] if dq else -1)
