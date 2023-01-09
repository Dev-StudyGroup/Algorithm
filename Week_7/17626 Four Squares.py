import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        j = 1
        min_value = int(1e9)
        while (j ** 2) <= i:
            min_value = min(min_value, dp[i - (j ** 2)])
            j += 1

        dp[i] = min_value + 1
    print(dp[n])
