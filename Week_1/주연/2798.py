n, m = map(int, input().split())
AList = list(map(int, input().split()))
BList = []
print(AList[4], len(AList))
for i in range(n):
    for x in range(i+1, n):
        for y in range(x+1, n):
            if AList[i] + AList[x] + AList[y] > m:
                continue
            else:
                BList.append(AList[i] + AList[x] + AList[y])

print(max(BList))