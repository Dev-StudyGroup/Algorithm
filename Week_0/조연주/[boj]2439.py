"""
별 찍기 - 2
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
n = int(input())

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)