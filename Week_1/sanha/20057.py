N = int(input())
sands = [list(map(int, input().split())) for _ in range(N)]
answer = 0
dxs = [0, 1, 0, -1]
dys = [-1, 0, 1, 0]
sx, sy = N // 2, N // 2
move = 0

left = [(-1, 0, 0.07), (1, 0, 0.07), (-1, -1, 0.1), (1, -1, 0.1), (-1, 1, 0.01),
        (1, 1, 0.01), (0, -2, 0.05), (-2, 0, 0.02), (2, 0, 0.02), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]

dic = {0: left, 1: down, 2: right, 3: up}

def in_boundary(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

def spread(x, y, directions):
    global answer

    total = 0
    if y < 0:
        return
    for dx, dy, z in directions:
        nx = x + dx
        ny = y + dy

        if z == 0:
            if in_boundary(nx, ny):
                sands[nx][ny] += sands[x][y] - total
            else:
                answer += sands[x][y] - total
        else:
            new_sand = int(sands[x][y] * z)
            if in_boundary(nx, ny):
                sands[nx][ny] += new_sand
            else:
                answer += new_sand
            total += new_sand

for i in range(N * 2 - 1):
    d = i % 4
    if d == 0 or d == 2:
        move += 1
    for _ in range(move):
        nx = sx + dxs[d]
        ny = sy + dys[d]
        spread(nx, ny, dic[d])
        sx, sy = nx, ny

print(answer)
