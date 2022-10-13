from collections import deque


n = int(input())

cards = [i for i in range(1, n+1)]
cards = deque(cards)

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards.popleft())
