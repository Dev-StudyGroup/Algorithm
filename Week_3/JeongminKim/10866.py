"""

    정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

    push_front X: 정수 X를 덱의 앞에 넣는다.
    push_back X: 정수 X를 덱의 뒤에 넣는다.
    pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    size: 덱에 들어있는 정수의 개수를 출력한다.
    empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
    front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

"""

from collections import deque
import sys

N = int(input())
d = deque()
for _ in range(N):
    temp = sys.stdin.readline().split()
    if len(temp) == 2:
        method = temp[0]
        value = int(temp[1])
    if len(temp) == 1:
        method = temp[0]

    if method == 'push_front':
        d.appendleft(value)

    if method == 'push_back':
        d.append(value)

    if method == 'pop_front':
        if d:
            print(d.popleft())
        else:
            print(-1)

    if method == 'pop_back':
        if d:
            print(d.pop())
        else:
            print(-1)

    if method == 'size':
        print(len(d))

    if method == 'empty':
        if d:
            print(0)
        else:
            print(1)

    if method == 'front':
        if d:
            print(d[0])
        else:
            print(-1)

    if method == 'back':
        if d:
            print(d[-1])
        else:
            print(-1)
