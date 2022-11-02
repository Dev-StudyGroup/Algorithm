#입력
n, m, b = map(int, input().split())
arr=[]
for i in range(n):
    arr+=list(map(int, input().split()))

#집터에서 가장 낮은 높이와 가장 높은 높이 찾기
max_h = max(arr)
min_h = min(arr)

#걸리는 시간, 높이
time=n*m*256*2
height=0
#높이를 i로 맞출 때 걸리는 시간 계산
for i in range(min_h, max_h+1):
    ans=0
    if i*(n*m)-sum(arr)>b:
        break
    for j in arr:
        if j==i:
            continue
        elif j > i:
            ans+=2*(j-i)
            if ans>time:
                break
        elif j<i:
            ans+=1*(i-j)
            if ans>time:
                break
    
    if time==-1 or ans<=time:
        time=ans
        height=i


#출력
print(time, height)
