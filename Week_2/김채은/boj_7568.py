n = int(input())
size = [list(map(int, input().split())) for _ in range(n)]

rank = []

for i in range(n):
    bigger_than_i = 0

    for j in range(n):
        if i == j:
            continue

        if size[i][0] < size[j][0] and size[i][1] < size[j][1]:
            bigger_than_i += 1

    rank.append(bigger_than_i + 1)

print(*rank)
