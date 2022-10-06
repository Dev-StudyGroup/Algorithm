'''
'숫자 카드 2'
'''
from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))
card_dict = defaultdict(int)
for i in card:
    card_dict[i] += 1

M = int(input())
sangeun = list(map(int, input().split()))

for i in sangeun:
    print(card_dict[i], end = ' ')
