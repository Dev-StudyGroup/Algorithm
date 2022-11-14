"""

    0 <= N, K <= 100,000

    +1 , -1

    *2
    수빈이의 위치가 동생의 위치보다 작다면 +
    수빈이의 위치가 동생의 위치보다 크다면 -

"""
from collections import deque

N, M = map(int, input().split())
point = N
remain = abs(M - N)
MAX = 10 ** 5
time = 0
dp = [0] * (MAX + 1)
queue = deque()
queue.append(point)
result = []
while queue:
    cur_point = queue.popleft()
    if cur_point == M:
        print(dp[cur_point])
        break
    time += 1
    for dx in (cur_point - 1, cur_point + 1, cur_point * 2):
        if 0 <= dx <= MAX and not dp[dx]:
            queue.append(dx)
            dp[dx] = dp[cur_point] + 1
