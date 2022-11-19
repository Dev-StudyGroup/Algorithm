N, M = map(int, input().split())
numbers = list(map(int, input().split()))
total = 0
totals = [0]
for number in numbers:
    total += number
    totals.append(total)

for _ in range(M):
    a, b = map(int, input().split())
    print(totals[b] - totals[a - 1])
