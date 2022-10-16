N, M = map(int, input().split())
space = []
for _ in range(N):
    space.append(list(map(int, input().split())))
magics = []
for _ in range(M):
    magics.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
shark_x, shark_y = (N + 1) // 2 - 1, (N + 1) // 2 - 1
bomb_marble = [0, 0, 0]
indexing = {}


def init():
    depth = 1
    index = 0
    cnt = 0  # 같은 방향으로 이동한 수
    order = [2, 1, 3, 0]
    x, y = N // 2, N // 2
    d = 0
    while x > -1 and y > -1:
        indexing[index] = [x, y]
        x += dx[order[d]]
        y += dy[order[d]]
        cnt += 1
        index += 1
        if cnt == depth:
            if d % 2 == 1:  # 방향이 1,3(북,남)일 때 depth 1증가
                depth += 1
            d = (d + 1) % 4
            cnt = 0


def blizzard(dir, dist):
    for i in range(1, dist + 1):
        space[shark_x + dx[dir] * i][shark_y + dy[dir] * i] = 0


def move():
    start, end = 1, 2  # 투 포인터
    while start < N * N-1 and end <= N * N-1:
        while start < N * N-1:
            sx, sy = indexing[start]
            if space[sx][sy] == 0:
                break
            start += 1
        else:
            return
        if end <= start:
            end = start + 1
        while end <= N * N-1:
            ex, ey = indexing[end]
            if space[ex][ey]:
                break
            end += 1
        else:
            return
        space[sx][sy], space[ex][ey] = space[ex][ey], 0


def bomb():
    flag = False
    start, end = 1, 2
    cnt = 1  # 같은 번호의 연속된 구슬의 수
    while start < N * N-1 and end <= N * N-1:
        sx, sy = indexing[start]
        ex, ey = indexing[end]
        if space[sx][sy] == space[ex][ey]:
            cnt += 1
            end += 1
        else:
            if cnt >= 4:
                flag = True
                for i in range(start, end):
                    bx, by = indexing[i]
                    bomb_marble[space[bx][by] - 1] += 1
                    space[bx][by] = 0
            cnt = 1
            start = end
            end = start + 1
    return flag


def change():
    global space
    new_space = [[0] * N for _ in range(N)]
    start, end = 1, 2
    index = 1
    cnt = 1  # 같은 번호의 연속된 구슬의 수
    while start < N * N-1 and end <= N * N-1:
        sx, sy = indexing[start]
        ex, ey = indexing[end]
        if space[sx][sy] == space[ex][ey]:
            cnt += 1
            end += 1
        else:
            ix, iy = indexing[index]
            new_space[ix][iy] = cnt
            ix, iy = indexing[index + 1]
            new_space[ix][iy] = space[sx][sy]
            index += 2
            cnt = 1
            start = end
            end = start + 1
        if index >= N * N:
            break
    space = new_space


init()
for magic in magics:
    d, s = magic
    blizzard(d-1, s)
    move()
    while bomb():
        move()
    change()

print(1*bomb_marble[0]+2*bomb_marble[1]+3*bomb_marble[2])
