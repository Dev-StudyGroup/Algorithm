N, M, K = map(int, input().split())
G = [[[] for _ in range(N)] for _ in range(N)]
fire_balls = [list(map(int, input().split())) for _ in range(M)]
dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]
answer = 0

for _ in range(K):
    if len(fire_balls) == 0:
        break

    while fire_balls:
        r, c, m, s, d = fire_balls.pop()
        nr = (r + dxs[d] * s) % N
        nc = (c + dys[d] * s) % N
        G[nr - 1][nc - 1].append((m, s, d))

    for i in range(N):
        for j in range(N):
            if len(G[i][j]) > 1:
                total_m, total_s, even_d, odd_d, cnt = 0, 0, 0, 0, len(G[i][j])
                while G[i][j]:
                    m, s, d = G[i][j].pop()
                    total_m += m
                    total_s += s
                    if d % 2 == 0:
                        even_d += 1
                    else:
                        odd_d += 1

                if total_m // 5:
                    if even_d == cnt or odd_d == cnt:
                        nd = [0, 2, 4, 6]
                    else:
                        nd = [1, 3, 5, 7]
                    for d in nd:
                        fire_balls.append((i, j, total_m // 5, total_s // cnt, d))
            elif len(G[i][j]) == 1:
                m, s, d = G[i][j].pop()
                fire_balls.append((i, j, m, s, d))

for fire_ball in fire_balls:
    answer += fire_ball[2]
print(answer)
