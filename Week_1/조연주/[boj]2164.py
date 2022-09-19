"""
카드2
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
from collections import deque

n = int(input())
card = deque([x for x in range(1, n + 1)])

while n > 1:
    card.popleft()
    n -= 1
    if n == 1:
        break
    card.append(card.popleft())

print(card[0])
