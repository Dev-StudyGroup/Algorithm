if __name__ == "__main__":
    N = int(input())
    dp = [1] * (N + 1)
    for i in range(1, (N + 1)):
        dp[i] = i * dp[i - 1]
    count = 0
    num = dp[N]
    num = list(str(num))
    while len(num) > 0:
        if not int(num.pop()):
            count += 1
        else:
            break
    print(count)
