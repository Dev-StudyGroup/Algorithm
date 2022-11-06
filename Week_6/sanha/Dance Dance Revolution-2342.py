import sys
sys.setrecursionlimit(10**6)

commands = list(map(int, input().split()))
dp = [[[-1] * 5 for _ in range(5)] for _ in range(100000)]

def move(cur, target):
    if cur == target:
        return 1
    if cur == 0:
        return 2
    if abs(cur - target) == 2:
        return 4
    return 3

def dfs(depth, left, right):
    if depth == len(commands) - 1:
        return 0

    if dp[depth][left][right] != -1:
        return dp[depth][left][right]

    dp[depth][left][right] = min(dfs(depth + 1, commands[depth], right) + move(left, commands[depth]),
                                 dfs(depth + 1, left, commands[depth]) + move(right, commands[depth]))
    return dp[depth][left][right]

print(dfs(0, 0, 0))
