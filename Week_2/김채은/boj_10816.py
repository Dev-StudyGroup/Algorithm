from collections import defaultdict

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

card_dict = defaultdict(int)

for card in cards:
    card_dict[card] += 1

answer = []

for c in check:
    answer.append(card_dict[c])

print(*answer)
