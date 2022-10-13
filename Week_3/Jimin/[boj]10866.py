'''
'덱'
'''
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()

for i in range(N):
    command = input()
    lenQueue = len(queue)

    if 'push_front' in command:
        command, num = command.split()
        queue.appendleft(int(num))

    elif 'push_back' in command:
        command, num = command.split()
        queue.append(int(num))

    elif command == 'pop_front\n':
        if lenQueue == 0:
            print(-1)
        else:
            pop_num = queue.popleft()
            print(pop_num)

    elif command == 'pop_back\n':
        if lenQueue == 0:
            print(-1)
        else:
            pop_num = queue.pop()
            print(pop_num)

    elif command == 'size\n':
        print(lenQueue)

    elif command == 'empty\n':
        if lenQueue == 0:
            print(1)
        else:
            print(0)

    elif command == 'front\n':
        if lenQueue == 0:
            print(-1)
        else:
            print(queue[0])

    else:
        if lenQueue == 0:
            print(-1)
        else:
            print(queue[-1])
