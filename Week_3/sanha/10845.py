import sys
from collections import deque

input = sys.stdin.readline
q = deque()

N = int(input())

for _ in range(N):
    command = input().rstrip()
    if 'push' in command:
        value = command.split()
        q.append(value[1])
    if command == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    if command == 'size':
        print(len(q))
    if command == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    if command == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    if command == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])
