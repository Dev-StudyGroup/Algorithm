from itertools import combinations
#입력
n, m = map(int, input().split())
num=list(map(int, input().split()))

#문제유형 파악 -> 조합을 이용한 구현

#구현
max=0
for i in combinations(num, 3):
    if sum(i)>m:
        continue
    elif max<sum(i):
        max=sum(i)
print(max)
