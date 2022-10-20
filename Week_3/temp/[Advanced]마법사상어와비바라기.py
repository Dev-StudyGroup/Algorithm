n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
command = []
for _ in range(m):
    command.append(tuple(map(int, input().split())))

dx, dy = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]
dcx, dcy = [-1, -1, 1, 1], [-1, 1, -1, 1]

def moveCloud(cloud, d, s):
    new_cloud = []

    for x, y in cloud:
        nx, ny =(x + dx[d-1] * s) % n, (y + dy[d-1] * s) % n
        new_cloud.append((nx, ny))

    return new_cloud


def raining(cloud):
    for x, y in cloud:
        data[x][y] += 1


def copyWater(cloud):
    copied_data = data[:]

    for x, y in cloud:
        for i in range(4):
            nx, ny = x + dcx[i], y + dcy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if data[nx][ny]:
                copied_data[x][y] += 1

    return copied_data


def makeCloud(cloud):
    new_cloud = []

    for i in range(n):
        for j in range(n):

            if (i, j) in cloud:
                continue

            if data[i][j] >= 2:
                data[i][j] -= 2
                new_cloud.append((i, j))

    return new_cloud


cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
for d, s in command:
    cloud = moveCloud(cloud, d, s)

    raining(cloud)

    data = copyWater(cloud)

    cloud = makeCloud(cloud)

result = 0
for i in range(n):
    result += sum(data[i])

print(result)