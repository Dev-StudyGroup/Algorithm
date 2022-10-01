"""

    숫자 카드 N개

    정수 M개가 주어졌을 때, 이 수가 적혀는 있는 숫자 카트를
    상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시요

"""
from collections import Counter

N = int(input())
cards = list(map(int, input().split()))
cards = Counter(cards)
M = int(input())
integer = list(map(int, input().split()))

for i in integer:
    print(cards[i], end=' ')

