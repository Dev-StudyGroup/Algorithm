'''
'괄호'
'''
from collections import deque

T = int(input())
for i in range(T):
    test = input()
    stack = deque()
    answer = 'YES'
    for i in test:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                pop = stack.pop()
                if pop == '(':
                    continue
                else:
                    answer = 'NO'
                    break
            else:
                answer = 'NO'
                break

    if answer == 'YES':
        if stack:
            answer = 'NO'
    print(answer)