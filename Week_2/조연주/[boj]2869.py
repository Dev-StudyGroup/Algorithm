"""
달팽이는 올라가고 싶다
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
from math import ceil

a, b, v = map(int, input().split())
print(ceil((v - a) / (a - b)) + 1)
