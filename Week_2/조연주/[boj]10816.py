"""
숫자 카드 2
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
from collections import Counter

n = int(input())
num_card = list(map(int, input().split()))
m = int(input())
find_card = list(map(int, input().split()))

c = Counter(num_card)

for num in find_card:
    print(c[num], end=' ')
