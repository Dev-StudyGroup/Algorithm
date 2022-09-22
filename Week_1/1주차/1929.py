import math

#입력
m, n = map(int, input().split())

#에라토스테네스의 체
arr=[False, False]+[True]*(n-1)

for i in range(2, int(math.sqrt(n))+1):
    if arr[i]:
        for j in range(2*i, n+1, i):
            arr[j]=False
#출력
for i in range(m, n+1):
    if arr[i]:
        print(i)
