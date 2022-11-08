"""
덱
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    command = list(sys.stdin.readline().split())
    if command[0] == "push_back":
        queue.append(int(command[1]))
    elif command[0] == "push_front":
        queue.appendleft(int(command[1]))
    elif command[0] == "pop_front":
        if len(queue) > 0:
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == "pop_back":
        if len(queue) > 0:
            print(queue.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if len(queue) > 0:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == "back":
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)
