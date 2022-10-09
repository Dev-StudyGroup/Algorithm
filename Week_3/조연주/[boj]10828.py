"""
스택
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
import sys

n = int(sys.stdin.readline()) # input() 사용 시 시간초과
stack = []

for _ in range(n):
    command = list(sys.stdin.readline().split())
    if command[0] == "push":
        stack.append(int(command[1]))
    elif command[0] == "pop":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif command[0] == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
