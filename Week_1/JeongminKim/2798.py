"""

    블랙잭
    1. 카드의 합이 21이 넘지 않도록 한다.
    2. 제일 크면 이김

    카드에는 양의 정수가 쓰여있음

    N장의 카드를 모두 숫자가 보이도록 바닥에 놓음
    N장의 카드 중 3장의 카드를 고르고, 고른 카드들의 합이 M보다 작으면서 최대한 가깝게 만들어야함

"""
import sys

result = []
selected = []

N, M = map(int, input().split())

cards = list(map(int, sys.stdin.readline().split()))

from itertools import permutations
card_comb = permutations(cards, 3)
s = 0
for comb in card_comb:
    if sum(comb) <= M:
        if s <= sum(comb):
            s = sum(comb)

print(s)

