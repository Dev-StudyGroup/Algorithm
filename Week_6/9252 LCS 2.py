import sys

input = sys.stdin.readline
if __name__ == "__main__":
    result = ""
    str1 = input().rstrip()
    str2 = input().rstrip()
    length = 0
    dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                continue
            if str1[i - 1] != str2[j - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    x, y = len(str1), len(str2)
    while x != 0 and y != 0:
        if dp[x - 1][y] == dp[x][y]:
            x -= 1
            continue
        if dp[x][y - 1] == dp[x][y]:
            y -= 1
            continue

        result += str1[x - 1]
        x -= 1
        y -= 1

    print(dp[len(str1)][len(str2)])
    print(result[::-1])
