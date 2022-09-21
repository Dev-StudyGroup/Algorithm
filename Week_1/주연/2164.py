n = int(input())
AList = []
for i in range(1, n+1):
    AList.append(i)

while len(AList) > 1:
    AList.pop(0)
    AList.append(AList.pop(0))

print(AList[0])