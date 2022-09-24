import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())
fire_ball = []
space = [[[] for _ in range(N)] for _ in range(N)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fire_ball.append((r, c, m, s, d))


def move():
    while fire_ball:
        fr, fc, fm, fs, fd = fire_ball.pop(0)
        nfr = (fr + (dx[fd] * fs)) % N
        nfc = (fc + (dy[fd] * fs)) % N
        space[nfr][nfc].append([fm, fs, fd])


for k in range(K):
    move()
    for i in range(N):
        for j in range(N):
            if len(space[i][j]) > 1:
                fire_ball_count = len(space[i][j])
                sum_m, sum_s, iseven, isodd = 0, 0, 0, 0
                while space[i][j]:  # if space is not null
                    now_m, now_s, now_d = space[i][j].pop(0)
                    sum_m += now_m
                    sum_s += now_s
                    if now_d % 2 == 0:
                        iseven += 1
                    else:
                        isodd += 1
                new_m = sum_m // 5
                new_s = sum_s // fire_ball_count
                if new_m > 0:
                    if iseven > 0 and isodd > 0:
                        for new_d in [1, 3, 5, 7]:
                            fire_ball.append((i, j, new_m, new_s, new_d))
                    else:
                        for new_d in [0, 2, 4, 6]:
                            fire_ball.append((i, j, new_m, new_s, new_d))
            elif len(space[i][j]) == 1:
                fire_ball.append([i, j] + space[i][j].pop(0))
print(sum([fb[2] for fb in fire_ball]))
