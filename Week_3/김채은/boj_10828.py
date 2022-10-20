from typing import Final
import sys

input = sys.stdin.readline

n = int(input().strip())

PUSH: Final = 'push'
TOP: Final = 'top'
SIZE: Final = 'size'
EMPTY: Final = 'empty'
POP: Final = 'pop'

stack = []

for _ in range(n):
    order_str = list(input().split())

    order = order_str[0]

    if order == PUSH:
        stack.append(order_str[1])

    elif order == TOP:
        stack_top = stack[-1] if stack else -1
        print(stack_top)

    elif order == SIZE:
        print(len(stack))

    elif order == EMPTY:
        isEmpty = 0 if stack else 1
        print(isEmpty)

    elif order == POP:
        stack_pop = stack.pop() if stack else -1
        print(stack_pop)
