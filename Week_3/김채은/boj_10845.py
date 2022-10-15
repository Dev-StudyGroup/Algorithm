from collections import deque
from typing import Final
import sys

input = sys.stdin.readline

n = int(input().strip())

PUSH: Final = 'push'
POP: Final = 'pop'
SIZE: Final = 'size'
EMPTY: Final = 'empty'
FRONT: Final = 'front'
BACK: Final = 'back'

dq = deque()

for _ in range(n):
    order_str = list(input().split())

    order = order_str[0]


    if order == PUSH:
        dq.append(order_str[1])

    elif order == POP:
        dq_popleft = dq.popleft() if dq else -1
        print(dq_popleft)

    elif order == SIZE:
        print(len(dq))

    elif order == EMPTY:
        isEmpty = 0 if dq else 1
        print(isEmpty)

    elif order == FRONT:
        dq_front = dq[0] if dq else -1
        print(dq_front)

    elif order == BACK:
        dq_back = dq[-1] if dq else -1
        print(dq_back)
