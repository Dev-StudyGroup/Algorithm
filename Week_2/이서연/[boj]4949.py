'''
균형잡힌 세상

- 문제 요약
어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램.
문자열에 포함되는 괄호는 소괄호()와 대괄호[] 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.
    - 모든 왼쪽 소괄호는 오른쪽 소괄호와만 짝을 이뤄야 한다.
    - 모든 왼쪽 대괄호는 오른쪽 대괄호와만 짝을 이뤄야 한다.
    - 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
    - 모든 괄호들의 짝은 1:1 매칭만 가능
    - 짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.

- 입력 조건
하나 또는 여러 줄에 걸쳐서 문자열이 주어진다. 각 문자열은 영문 알파벳, 공백, 소괄호, 대괄호 등으로 이루여져 있으며 길이는 100보다 작거나 같다.
각 줄은 마침표로 끝난다.
입력의 종료 조건으로 맨 마지막에 점 하나가 들어온다.

- 출력 조건
각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력
'''
import sys

while True:
    str = sys.stdin.readline().rstrip()
    if str == '.':
        break
    small_left = str.count('(')
    small_right = str.count(')')
    big_left = str.count('[')
    big_right = str.count(']')
    
    if small_left == small_right and big_left == big_right:
        stack = []
        i = 0
        while i < len(str):
            if str[i] == '(':
                stack.append(')')
            elif str[i] == '[':
                stack.append(']')
            elif str[i] == ')' or  str[i] == ']':
                if stack:
                    if str[i] != stack.pop():
                        print('no')
                        break
                else:
                    print('no')
                    break
            i += 1
        
        if i == len(str):
            print('yes')

    else:
        print('no')
