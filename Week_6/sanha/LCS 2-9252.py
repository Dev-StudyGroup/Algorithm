a = list(map(str, input()))
b = list(map(str, input()))
len_a = len(a)
len_b = len(b)
dp = [[''] * (len_b + 1) for _ in range(len_a + 1)]

for i in range(1, len_a + 1):
    for j in range(1, len_b + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + a[i - 1]
        elif len(dp[i - 1][j]) >= len(dp[i][j - 1]):
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i][j - 1]

if len(dp[-1][-1]) == 0:
    print(0)
else:
    print(len(dp[-1][-1]))
    print(dp[-1][-1])
