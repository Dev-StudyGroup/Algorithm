"""

    N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수 구하는 프로그램

"""
N = int(input())
dp = [0] * (N + 1)
dp[0] = 1
for i in range(1, N + 1):
    if i == 1:
        dp[i] = i
    else:
        dp[i] = dp[i - 1] * i

n_fact = str(dp[N])[::-1]
count = 0
for number in n_fact:
    if int(number) == 0:
        count += 1
    else:
        break

print(count)
