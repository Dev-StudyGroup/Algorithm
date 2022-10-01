from collections import deque
import sys

N = int(input())
q = deque()
count = 0
for _ in range(N):
    s = sys.stdin.readline().split()
    if s[0] == "push":
        q.append(int(s[1]))
        count += 1
    elif s[0] == "pop":
        if count > 0:
            print(q.pop())
            count -= 1
        else:
            print(-1)
    elif s[0] == "size":
        print(count)
    elif s[0] == "empty":
        if count == 0:
            print(1)
        else:
            print(0)
    elif s[0] == "top":
        if count > 0:
            print(q[count-1])
        else:
            print(-1)
