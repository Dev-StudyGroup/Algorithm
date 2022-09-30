"""
문자열 반복
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
t = int(input())

for i in range(t):
    r, s = input().split()
    result = ''
    for x in list(s):
        result += x * int(r)
    print(result)


