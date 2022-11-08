'''
'스택'
'''
import sys
input = sys.stdin.readline

N = int(input())
stack = []

for i in range(N):
    command = input()
    lenStack = len(stack)

    if ' ' in command:
        command, num = command.split()
        stack.append(int(num))

    elif command == 'pop\n':
        if lenStack == 0:
            print(-1)
        else:
            pop_num = stack.pop()
            print(pop_num)

    elif command == 'size\n':
        print(lenStack)

    elif command == 'empty\n':
        if lenStack == 0:
            print(1)
        else:
            print(0)

    else:
        if lenStack == 0:
            print(-1)
        else:
            print(stack[-1])
