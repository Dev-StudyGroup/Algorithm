import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    arr = input().rstrip()[1:-1].split(',')

    if arr == ['']:
        q = deque()
    else:
       q = deque(list(map(int, arr)))
    flag = False
    re = 1

    for command in p:
        if command == 'D':
            if not q:
                flag = True
                break
            if re > 0:
                q.popleft()
            else:
                q.pop()
        else:
            re *= -1

    if flag:
        print("error")
    else:
        if re < 0:
            q = list(q)[::-1]

        print('[', end='')
        for i in range(len(q)):
            print(q[i], end='')
            if i != len(q) - 1:
                print(',', end='')
        print(']')
