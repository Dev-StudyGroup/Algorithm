import sys
N, M, B = map(int, sys.stdin.readline().split())
space = []
# max_height, min_height = 0, 257
summary = B
for _ in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    summary += sum(a)
    space.append(a)
max_height = (summary+B)//(M*N)
h = 0
result = []
while h <= max_height:
    temp = B
    time = 0
    for i in space:
        for j in i:
            if j >= h:
                time += 2 * (j - h)
                temp += (j - h)
            else:
                time += (h - j)
                temp -= (h - j)
    if temp >= 0:
        result.append([time, h])
    h += 1

result.sort(key=lambda x:(x[0],-x[1]))
print(*result[0])