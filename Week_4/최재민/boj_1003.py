t = int(input())

for _ in range(t):
    dp0 = [0] * 41
    dp1 = [0] * 41
    dp0[0] = 1
    dp0[1] = 0
    dp1[0] = 0
    dp1[1] = 1
    n = int(input())

    for i in range(2, n+1):
        dp0[i] = dp0[i-1] + dp0[i-2]
        dp1[i] = dp1[i-1] + dp1[i-2]

    print(dp0[n], dp1[n])
