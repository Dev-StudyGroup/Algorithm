"""
스택 수열
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
n = int(input())
now = 1
flag = True
stack = []
result = []

for i in range(n):
    num = int(input())
    while now <= num:
        stack.append(now)
        result.append('+')
        now += 1
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        flag = False

if flag:
    print(*result, sep='\n')
else:
    print("NO")
