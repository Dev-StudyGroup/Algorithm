N = int(input())
stairs = []
dp = [0] * N

for _ in range(N):
    point = int(input())
    stairs.append(point)

if N <= 2:
    if N == 2:
        print(stairs[0] + stairs[1])
    if N == 1:
        print(stairs[0])
else:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(3, N):
        dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])
    print(dp[N - 1])
