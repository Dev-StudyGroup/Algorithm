from collections import deque
N = int(input())
cards = deque(list(i for i in range(1, N + 1)))

while cards:
    if len(cards) == 1:
        print(cards[0])
        break
    cards.popleft()
    cards.append(cards.popleft())
