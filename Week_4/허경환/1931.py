import sys
#입력
n = int(input())
timeline=[]
for i in range(n):
    i, j = map(int, input().split())
    timeline.append((i,j))

#정렬
timeline.sort(key=lambda x:(x[1], x[0]))

#반복문으로 회의 개수 카운트
count=0
last_end_time=0
for i in timeline:   
    if i[0]<last_end_time:
        continue
    else:
        last_end_time=i[1]
        count+=1
#출력
print(count)
    
    
