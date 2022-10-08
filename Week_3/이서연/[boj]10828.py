'''
스택

- 문제 요약
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램.
명령은 총 다섯가지.
    - push X: 정수 X를 스택에 넣는 연산
    - pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력. 만약 스택에 들어있는 정수가 없는 경우 -1 출력.
    - size: 스택에 들어있는 정수의 개수를 출력
    - empty: 스택이 비어있으면 1, 아니면 0을 출력
    - top: 스택의 가장 위에 있는 정수를 출력. 만약 스택에 들어있는 정수가 없는 경우 -1 출력

- 입력 조건
첫째 줄에 주어지는 명령의 수 N(1 <= N <= 10,000)이 주어진다.
둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 
주어지는 정수는 1 이상 100,000 이하

- 출력 조건
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력
'''
import sys
n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == 'push':
        stack.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
