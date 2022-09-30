"""
블랙잭
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
minus = m
result = 0

card_list = list(combinations(cards, 3))

for l in card_list:
    if sum(l) > m:
        continue
    else:
        if minus > m - sum(l):
            minus = m - sum(l)
            result = sum(l)

print(result)
