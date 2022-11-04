import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    dp = [0] * (N + 1)
    dp[0] = arr[0]
    dp[1] = dp[0] + arr[1]
    index = 2
    count = 1
    while index <= N - 1:
        print(index, count)
        if arr[index - 1] >= arr[index - 2]:
            count += 1
            if count == 3:
                dp[index] = arr[index] + dp[index - 2]
                count = 1
            else:
                dp[index] = arr[index] + dp[index - 1]
        else:
            dp[index] = arr[index] + dp[index - 2]
            count = 1
        index += 1
    # print(index, count)
    print(arr)
    print(dp)
