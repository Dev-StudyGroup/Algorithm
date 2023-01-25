import sys

input = sys.stdin.readline
MAX = int(1e9)


def calculate_power(command, position):
    if position == 0:
        return 2
    if position == command:
        return 1
    if abs(command - position) == 2:
        return 4
    return 3


if __name__ == "__main__":
    commands = list(map(int, input().split()))
    result = MAX + 1
    commands_length = len(commands) - 1
    dp = [[[MAX for _ in range(5)] for _ in range(5)] for _ in range(commands_length + 1)]
    dp[-1][0][0] = 0
    for i in range(commands_length):
        for r in range(5):
            for l in range(5):
                power = calculate_power(commands[i], l)
                dp[i][commands[i]][r] = min(dp[i][commands[i]][r], dp[i - 1][l][r] + power)

        for l in range(5):
            for r in range(5):
                power = calculate_power(commands[i], r)
                dp[i][l][commands[i]] = min(dp[i][l][commands[i]], dp[i - 1][l][r] + power)

    for l in range(5):
        for r in range(5):
            result = min(result, dp[commands_length - 1][l][r])
    print(result)
