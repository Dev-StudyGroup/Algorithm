#입력
k, n = map(int, input().split())
lan=[]
for i in range(k):
    lan.append(int(input()))

ans = 0

#필요한 만큼의 랜선을 만들 수 있는지 판단하는 함수
def make_lan(length):
    count=0
    for i in lan:
        count+=i//length
    if count>=n:
        return True
    else:
        return False
    
#매개변수 탐색
start=1
end=2**31-1

while start<=end:
    mid=(start+end)//2
    if make_lan(mid):
        start=mid+1
    else:
        end=mid-1

ans=end

#출력
print(ans)
