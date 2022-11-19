n = int(input())

dp = [0] * 1001
dp[1], dp[2], dp[3], dp[4] = 1, 2, 3, 5

for i in range(4, n + 1):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 10007

print(dp[n])
