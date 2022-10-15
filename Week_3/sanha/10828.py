import sys
input = sys.stdin.readline
N = int(input())
stack = []

for _ in range(N):
    command = input().rstrip()
    if ' ' in command:
        push = command.split()
        stack.append(push[1])
        continue
    if command == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
        continue
    if command == "size":
        print(len(stack))
        continue
    if command == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
        continue
    if command == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
