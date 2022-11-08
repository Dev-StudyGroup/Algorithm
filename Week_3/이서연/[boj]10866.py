'''
덱

- 문제 요약
정수를 저장하는 덱(Deque)을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램.
명령은 총 여덟가지.
    - push_front X: 정수 X를 덱의 앞에 넣는다.
    - push_back X: 정수 X를 덱의 뒤에 넣는다.
    - pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력. 만약 덱에 들어있는 정수가 없는 경우 -1 출력.
    - pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력. 만약 덱에 들어있는 정수가 없는 경우 -1 출력.
    - size: 덱에 들어있는 정수의 개수를 출력
    - empty: 덱이 비어있으면 1, 아니면 0을 출력
    - front: 덱의 가장 앞에 있는 정수를 출력. 만약 덱에 들어있는 정수가 없는 경우 -1 출력
    - back: 덱의 가장 뒤에 있는 정수를 출력. 만약 덱에 들어있는 정수가 없는 경우 -1 출력

- 입력 조건
첫째 줄에 주어지는 명령의 수 N(1 <= N <= 10,000)이 주어진다.
둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 
주어지는 정수는 1 이상 100,000 이하

- 출력 조건
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력
'''
import sys
n = int(sys.stdin.readline())
deque = []
for _ in range(n):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == 'push_front':
        deque.insert(0, int(cmd[1]))
    elif cmd[0] == 'push_back':
        deque.append(int(cmd[1]))
    elif cmd[0] == 'pop_front':
        if deque:
            print(deque.pop(0))
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(deque))
    elif cmd[0] == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if deque:
            print(deque[-1])
        else:
            print(-1)
