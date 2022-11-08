import sys
#입력
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
broken = list(sys.stdin.readline().rstrip().split())

#버튼누를 횟수 저장할 변수 ans
ans = abs(n-100)

#0~1000000 범위의 숫자를 모두 확인하여 가장 버튼누르는 횟수가 적은 걸로 갱신
for i in range(1000001):
    flag=False
    for j in str(i):
        if j in broken:
            flag=True
            break
    if flag==False:
        ans=min(ans, len(str(i))+abs(i-n))
#출력
print(ans)
