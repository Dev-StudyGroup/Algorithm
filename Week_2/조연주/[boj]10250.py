"""
ACM 호텔
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
from math import ceil

t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    floor = n % h
    if floor == 0:
        floor = h
    num = ceil(n / h)
    str_num = ''
    if num < 10:
        str_num = '0' + str(num)
    else:
        str_num = str(num)
    print(str(floor) + str_num)
