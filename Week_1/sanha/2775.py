T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    dp = [i for i in range(n + 1)]
    for i in range(k):
        for j in range(1, n + 1):
            dp[j] += dp[j - 1]

    print(dp[-1])
