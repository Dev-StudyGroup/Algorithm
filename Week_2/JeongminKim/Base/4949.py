"""

    모든 왼쪽 소괄호는 오른쪽 소괄호와만 짝을 이뤄야 한다.
    모든 왼쪽 대괄호는 오른쪽 대괄호와만 짝을 이뤄야 한다.
    모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
    모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
    짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.

"""

import re
import sys


def check_bracket(s):
    match = {'(': ')', '[': ']', ')': '(', ']': '['}
    answer = True
    if len(s) == 0:
        return True
    # 여는 괄호를 담는 stack
    open_bracket = []
    for i in s:
        if i == '(' or i == '[':
            open_bracket.append(i)
        else:
            if len(open_bracket) == 0:
                return False
            else:
                if open_bracket[-1] == match[i]:
                    open_bracket.pop(-1)
                else:
                    return False
    if len(open_bracket) > 0:
        return False
    return answer


while 1:
    s = input().rstrip()

    if s == '.':
        break

    s = re.sub('[0-9A-Za-z .]+', '', s)

    if check_bracket(s):
        print('yes')
    else:
        print('no')
