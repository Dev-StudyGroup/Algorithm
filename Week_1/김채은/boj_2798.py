from itertools import combinations

n, m = map(int, input().split())

cards = list(map(int, input().split()))

answer = 0

for comb in list(combinations(cards, 3)):
    _sum = sum(comb)
    if _sum <= m:
        answer = max(answer, _sum)

print(answer)
