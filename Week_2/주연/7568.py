n = int(input())
arr = []

for _ in range(n):
    weight, height = map(int, input().split())
    arr.append((weight, height))

for i in arr:
    rank = 1
    for x in arr:
        if i[0] < x[0] and i[1] < x[1]:
            rank += 1
    print(rank, end=" ")