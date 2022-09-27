"""

    N장의 카드
    1 ~ N까지 차례대로
    1번카드가 제일 위에,
    N번카드가 제일 아래

    카드가 한 장 남을 때까지 다음 동작을 반복한다.
        1. 제일 위에 있는 카드를 바닥에 버린다.
        2. 그 다음 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

    1234
    234
    342
    43
    24
    4


"""
from collections import deque

N = int(input())

cards = deque([i for i in range(1, N + 1)])

while len(cards) > 1:
    # 제일 위에 있는 카드를 바닥에 버린다.
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])
