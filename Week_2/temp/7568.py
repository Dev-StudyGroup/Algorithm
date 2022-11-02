#입력
n = int(input())
list=[]
for i in range(n):
    a, b = map(int, input().split())
    list.append((a,b))

#문제유형 -> 구현

#구현

for a, b in list:
    count=0
    for i, j in list:
        if a<i and b<j:
            count+=1
    print(count+1, end=' ')
