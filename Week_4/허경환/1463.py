#입력
n = int(input())

#다이나믹 프로그래밍
#최적부분구조인가? = 큰문제를 작은문제로 나눌 수 있고, 큰문제/작은문제를 같은 방법으로 해결할 수 있는가?
#중복되는 부분문제가 있는가?

#최종적으로 구할 큰 문제 = n
#큰문제와 작은문제간의 관계를 점화식으로 나타내기
# N = min(N-1, N//2, N//3) + 1

#dp테이블
dp = [0]*(n+1)
dp[1]=0
if n>=2:
    dp[2]=1
if n>=3:
    dp[3]=1

#bottom-up
for i in range(4, n+1):
    if i%3==0 and i%2==0:
        dp[i]=min(dp[i-1], dp[i//2], dp[i//3])+1
    elif i%3==0 and i%2!=0:
        dp[i]=min(dp[i-1], dp[i//3])+1
    elif i%3!=0 and i%2==0:
        dp[i]=min(dp[i-1], dp[i//2])+1
    else:
        dp[i]=dp[i-1]+1

#출력
print(dp[n])
