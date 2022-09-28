from bisect import bisect_left, bisect_right

n = int(input())
card = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

card.sort()
result = []
for t in target:
    idx1 = bisect_left(card, t)
    idx2 = bisect_right(card, t)
    result.append(idx2 - idx1)

print(*result, sep=' ')