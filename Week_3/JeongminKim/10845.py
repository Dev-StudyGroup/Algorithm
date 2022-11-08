"""

    push X: 정수 X를 큐에 넣는 연산이다.
    pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    size: 큐에 들어있는 정수의 개수를 출력한다.
    empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
    front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

"""
import sys

N = int(input())
q = []
for _ in range(N):
    temp = sys.stdin.readline().split()
    if len(temp) == 2:
        method = temp[0]
        value = int(temp[1])
    if len(temp) == 1:
        method = temp[0]

    if method == 'push':
        q.append(value)

    if method == 'pop':
        if q:
            print(q.pop(0))
        else:
            print(-1)
    if method == 'size':
        print(len(q))

    if method == 'empty':
        if q:
            print(0)
        else:
            print(1)

    if method == 'front':
        if q:
            print(q[0])
        else:
            print(-1)

    if method == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
