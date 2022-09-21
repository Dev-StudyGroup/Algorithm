n = int(input())
AList = []
for i in range(n):
    m = int(input())
    AList.append(m)

AList.sort()

for i in AList:
    print(i)