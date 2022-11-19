import sys

input = sys.stdin.readline

M = int(input())
arr = [False] * 21

for _ in range(M):
    x = 0
    operate = input().split()
    if len(operate) > 1:
        x = int(operate[1])
    operation = operate[0]

    if operation == 'add':
        arr[x] = True
    if operation == 'remove':
        arr[x] = False
    if operation == 'check':
        if arr[x]:
            print(1)
        else:
            print(0)
    if operation == 'toggle':
        if arr[x]:
            arr[x] = False
        else:
            arr[x] = True
    if operation == 'all':
        arr = [True] * 21
    if operation == 'empty':
        arr = [False] * 21
