N, M, B = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]

Min = min(map(min, G))
Max = max(map(max, G))
least_time = int(1e9)

for k in range(Min, Max + 1):
    plus_cnt = 0
    minus_cnt = 0
    for i in range(N):
        for j in range(M):
            h = G[i][j] - k
            if h < 0:
                plus_cnt -= h
            elif h > 0:
                minus_cnt += h
    if minus_cnt + B >= plus_cnt:
        time = minus_cnt * 2 + plus_cnt
        if least_time >= time:
            least_time = time
            result = k
print(least_time, result)
