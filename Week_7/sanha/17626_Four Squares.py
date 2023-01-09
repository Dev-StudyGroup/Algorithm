n = int(input())
INF = int(1e9)
answer = 0
dp = [0] * 50001
dp[1], dp[2] = 1, 2

for i in range(3, n + 1):
    Min = INF
    for j in range(1, int(i ** 0.5) + 1):
        Min = min(Min, dp[i - j ** 2])
    dp[i] = Min + 1

print(dp[n])
