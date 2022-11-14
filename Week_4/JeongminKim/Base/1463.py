"""

    정수 X에 사용할 수 있는 연산

    1. X % 3 == 0 => X /= 3
    2. X % 2 == 0 => X /= 2
    3. X -= 1

    3개의 연산을 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값은?

"""

num = int(input())
dp = [0] * (num + 1)

for i in range(2, num + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[num])
