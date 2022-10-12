N, M = map(int, input().split())
G = [list(input()) for _ in range(N)]
answer = 64

for i in range(N - 7):
    for j in range(M - 7):
        start_w_cnt = 0
        start_b_cnt = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    if G[x][y] != 'W':
                        start_b_cnt += 1
                    else:
                        start_w_cnt += 1
                else:
                    if G[x][y] != 'B':
                        start_b_cnt += 1
                    else:
                        start_w_cnt += 1
        answer = min(answer, min(start_w_cnt, start_b_cnt))

print(answer)
