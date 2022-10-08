'''
큐

- 문제 요약
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램.
명령은 총 여섯가지.
    - push X: 정수 X를 큐에 넣는 연산
    - pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력. 만약 큐에 들어있는 정수가 없는 경우 -1 출력.
    - size: 큐에 들어있는 정수의 개수를 출력
    - empty: 큐가 비어있으면 1, 아니면 0을 출력
    - front: 큐의 가장 앞에 있는 정수를 출력. 만약 큐에 들어있는 정수가 없는 경우 -1 출력
    - back: 큐의 가장 뒤에 있는 정수를 출력. 만약 큐에 들어있는 정수가 없는 경우 -1 출력

- 입력 조건
첫째 줄에 주어지는 명령의 수 N(1 <= N <= 10,000)이 주어진다.
둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 
주어지는 정수는 1 이상 100,000 이하

- 출력 조건
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력
'''
import sys
n = int(sys.stdin.readline())
queue = []
for _ in range(n):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == 'push':
        queue.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
