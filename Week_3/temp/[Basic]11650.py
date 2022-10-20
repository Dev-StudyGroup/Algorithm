n = int(input())
data = []
for _ in range(n):
    data.append(tuple(map(int, input().split())))

data.sort()
for i in range(n):
    print(data[i][0], data[i][1])