n = int(input())
Alist = list(map(int,input().split()))

decList = []
for i in Alist:
    cnt = 0
    for x in range(1, i + 1):
        if i == 1: cnt = 3
        if i % x == 0: cnt += 1
    if cnt <= 2:
        decList.append(i)

print(len(decList))