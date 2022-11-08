N = int(input())
space = []
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
left = [(0, -2, 0.05), (-1, -1, 0.1), (1, -1, 0.1), (-1, 0, 0.07), (1, 0, 0.07), (-2, 0, 0.02), (2, 0, 0.02),
        (-1, 1, 0.01), (1, 1, 0.01), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
for _ in range(N):
    space.append(list(map(int, input().split())))
x, y = N // 2, N // 2  # 토네이도 위치
result = 0


def scatter_sand(x, y, dir):
    global result
    total = 0
    for a, b, z in dir:
        if z == 0:
            new_sand = space[x][y] - total
        else:
            new_sand = int(space[x][y] * z)
            total += new_sand
        nx = x + a
        ny = y + b
        if 0 <= nx < N and 0 <= ny < N:
            space[nx][ny] += new_sand
        else:
            result += new_sand


def solution(x, y):
    c, d, count, m = 0, 0, 0, 1
    direction = {0: left, 1: down, 2: right, 3: up}
    while True:
        c += 1
        space[x][y] = 0
        x += dx[d]
        y += dy[d]
        scatter_sand(x, y, direction[d])

        if c == m:
            count += 1
            if count == 2:
                count = 0
                m += 1
            d = (d + 1) % 4
            c = 0
        if x == 0 and y == 0:
            break
    print(result)


solution(x, y)
