people = []
n = int(input())
for _ in range(n):
    people.append(tuple(map(int, input().split())))

result = []
for weight, hight in people:
    count = 0
    for w, h in people:
        if weight < w and hight < h:
            count += 1

    result.append(count+1)

for r in result:
    print(r , end=' ')