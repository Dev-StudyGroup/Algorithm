'''
'균형잡힌 세상'
'''
from collections import deque

while True:
    test = input()
    if test == '.':
        break
    stack = deque()
    answer = 'yes'
    for i in test:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack:
                pop = stack.pop()
                if pop == '(':
                    continue
                else:
                    answer = 'no'
                    break
            else:
                answer = 'no'
                break
        elif i == ']':
            if stack:
                pop = stack.pop()
                if pop == '[':
                    continue
                else:
                    answer = 'no'
                    break
            else:
                answer = 'no'
                break
    if answer == 'yes':
        if stack:
            answer = 'no'
    print(answer)
