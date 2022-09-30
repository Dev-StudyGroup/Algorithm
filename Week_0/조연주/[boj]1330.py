"""
두 수 비교하기
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
a,b = map(int, input().split())

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')