#입력
n, m = map(int, input().split())
tree=list(map(int, input().split()))

#문제유형파악 -> 매개변수 탐색

#범위설정
start=0
end=max(tree)
mid=0

#매개변수 탐색
while start+1<end:
    mid=(start+end)//2
    sum=0
    for i in tree:
        if i>mid:
            sum+=i-mid
    if sum>=m:
        start=mid
    else:
        end=mid

#출력
print(start)
