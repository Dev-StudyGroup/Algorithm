"""
수 찾기
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
from collections import Counter

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
c = Counter(a)

for x in b:
    if c[x]:
        print("1")
    else:
        print("0")
