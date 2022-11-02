from collections import defaultdict

N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
n2ball = [-1] * (N ** 2)
n2loc = defaultdict()
loc2n = defaultdict()
answer = 0
sx, sy = int(N / 2), int(N / 2)

def init_grid():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cnt = N ** 2 - 1
    dist = N
    dir = 0
    loc = (0, -1)
    while True:
        for i in range(dist):
            nx = loc[0] + dx[dir]
            ny = loc[1] + dy[dir]
            loc2n[(nx, ny)] = cnt
            n2loc[cnt] = (nx, ny)
            n2ball[cnt] = G[nx][ny]
            cnt -= 1
            loc = (nx, ny)
        dir = (dir + 1) % 4
        if dir == 1 or dir == 3:
            dist -= 1
        if dist == 0:
            break

def blizzard(d, s):
    dxs = ['no', -1, 1, 0, 0]
    dys = ['no', 0, 0, -1, 1]
    for i in range(1, s + 1):
        nx = sx + dxs[d] * i
        ny = sy + dys[d] * i
        n = loc2n[(nx, ny)]
        n2ball[n] = -1

def arrange():
    global n2ball
    del_cnt = n2ball.count(-1)
    n2ball = [ball for ball in n2ball if ball != -1]
    n2ball.extend([0] * del_cnt)

def bomb():
    global answer
    target, cnt = 0, 0
    ball_num = 0
    flag = False

    for i in range(N ** 2):
        if n2ball[i] == n2ball[target]:
            cnt += 1
        else:
            if cnt >= 4:
                flag = True
                for j in range(target, i):
                    n2ball[j] = -1
                answer += cnt * ball_num
            target = i
            cnt = 1
            ball_num = n2ball[i]
    return flag

def spread():
    global n2ball

    new_n2ball = [0]
    group = []
    for i in range(1, N ** 2):
        if not group:
            group.append(n2ball[i])
        elif group[0] == n2ball[i]:
            group.append(n2ball[i])
        else:
            new_n2ball.append(len(group))
            new_n2ball.append(group[0])
            group = [n2ball[i]]
    n2ball = [0] * (N ** 2)
    for i in range(len(new_n2ball)):
        if i >= (N ** 2):
            break
        n2ball[i] = new_n2ball[i]

init_grid()
for _ in range(M):
    d, s = map(int, input().split())
    blizzard(d, s)
    arrange()
    while True:
        if not bomb():
            break
        arrange()
    spread()
print(answer)
