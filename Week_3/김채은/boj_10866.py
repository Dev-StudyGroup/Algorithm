from collections import deque
from typing import Final
import sys

input = sys.stdin.readline

n = int(input().strip())

PUSH_FRONT: Final = 'push_front'
PUSH_BACK: Final = 'push_back'
POP_FRONT: Final = 'pop_front'
POP_BACK: Final = 'pop_back'
SIZE: Final = 'size'
EMPTY: Final = 'empty'
FRONT: Final = 'front'
BACK: Final = 'back'

dq = deque()

for _ in range(n):
    order_str = list(input().split())

    order = order_str[0]


    if order == PUSH_FRONT:
        dq.appendleft(order_str[1])

    if order == PUSH_BACK:
        dq.append(order_str[1])

    elif order == POP_FRONT:
        dq_popleft = dq.popleft() if dq else -1
        print(dq_popleft)

    elif order == POP_BACK:
        dq_popleft = dq.pop() if dq else -1
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
