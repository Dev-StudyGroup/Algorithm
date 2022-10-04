n = int(input())
nNum = list(map(int, input().split()))
m = int(input())
mNum = list(map(int, input().split()))

cntArr = []

for i in range(m):
    cnt = 0
    for x in range(n):
        if mNum[i] == nNum[x]:
            cnt += 1
    cntArr.append(cnt)

print(*cntArr)