import sys
from collections import Counter 
#입력
n = int(input())
num = []
sum=0
for i in range(n):
    m = int(sys.stdin.readline().rstrip())
    sum+=m
    num.append(m)
    
#산술평균
print(round(sum/len(num)))
#중앙값
num.sort()
print(num[len(num)//2])
#최빈값
counter = Counter(num)
order = counter.most_common()
maximum = order[0][1]
mod=[]
for i in order:
    if i[1]==maximum:
        mod.append(i)

mod.sort()
if len(mod)==1:
    print(mod[0][0])
else:
    print(mod[1][0])

#범위
print(max(num)-min(num))
