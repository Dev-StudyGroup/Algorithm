"""
10816: 숫자 카드2
"""
import sys
n = int(sys.stdin.readline())
cards = sorted(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for i in nums:
    if i in count:
        print(count[i], end=" ")
    else:
        print(0, end=" ")
