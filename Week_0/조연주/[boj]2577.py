"""
숫자의 개수
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
from collections import Counter

a = int(input())
b = int(input())
c = int(input())

l = list(str(a * b * c))
n = Counter(l)

for i in range(10):
    print(n[str(i)])