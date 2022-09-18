"""
숫자의 합
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
n = input()
l = list(input())
result = 0

for x in l:
    result += int(x)

print(result)