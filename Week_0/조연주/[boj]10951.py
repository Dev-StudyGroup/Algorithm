"""
A+B - 4
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
while 1:
    try:
        a, b = map(int, input().split())
    except:
        break
    print(a + b)