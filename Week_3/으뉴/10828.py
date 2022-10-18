import sys
input = sys.stdin.readline
stk = []

n = int(input())
orders = [input().rstrip() for _ in range(n)]

for order in orders:
    if 'push' in order:
        stk.append(order.split()[1])
    elif 'pop' in order:
        print(stk.pop() if stk else -1)
    elif 'size' in order:
        print(len(stk))
    elif 'empty' in order:
        print(0 if stk else 1)
    elif 'top' in order:
        print(stk[-1] if stk else -1)
