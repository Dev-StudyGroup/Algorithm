#입력
n = int(input())
inf=1e10
#구현 -> 3과 5의 최소공배수 = 15
#dp문제 -> 최적부분구조, 중복된 부분문제
#점화식 f(n)=min(f(n-3)+1, f(n-5)+1)

#bottom-up방식
#dp테이블
dp=[inf]*(n+1)
dp[3]=1

if n>=5:
    dp[5]=1

for i in range(6, n+1):
    if dp[i-3]==inf and dp[i-5]==inf:
        continue
    else:
        dp[i]=min(dp[i-3]+1, dp[i-5]+1)

#출력
if dp[n]==inf:
    print(-1)
else:
    print(dp[n])
