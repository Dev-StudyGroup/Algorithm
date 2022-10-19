n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
command = []
for _ in range(m):
    command.append(tuple(map(int, input().split())))
xy = (n) // 2

def destroyMarbles(d, s):
    ddx, ddy = [-1, 1, 0, 0], [0, 0, -1, 1]

    for i in range(1, s+1):
        nx, ny = xy + ddx[d-1] * i, xy + ddy[d-1] * i

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            break
        data[nx][ny] = 0
        

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
dt = [1, 0, 1, 0]

def moveMarbles():
    x, y, d, t, i = xy, xy, 0, 0, -1
    new_data = [[0]*n for _ in range(n)]
    path = []
    
    while 1:
        t += dt[d]
        for _ in range(t):
            x, y = x + dx[d], y + dy[d]

            if (x, y) == (0, -1):
                return new_data
            path.append((x, y))

            if data[x][y] == 0:
                i -= 1
                continue
            nx, ny = path[i]
            new_data[nx][ny] = data[x][y]

        d = (d + 1) % 4


def groupingMarbles():
    group, temp_group = [], []
    x, y, d, t = xy, xy, 0, 0

    while 1:
        t += dt[d]
        for _ in range(t):
            x, y = x + dx[d], y + dy[d]

            if (x, y) == (0, -1) or data[x][y] == 0:
                if len(temp_group):
                    group.append(temp_group)
                return group
            
            if len(temp_group) and data[temp_group[-1][0]][temp_group[-1][1]] != data[x][y]:
                group.append(temp_group)
                temp_group = []
            temp_group.append((x, y))

        d = (d + 1) % 4
            

def burstMarbles():
    count = {1: 0, 2: 0, 3: 0}
    groups = groupingMarbles()

    for group in groups:
        if len(group) >= 4:
            value = data[group[0][0]][group[0][1]]

            for x, y in group:
                data[x][y] = 0
                count[value] += 1

    return count


def transformMarbles():
    new_marbles = []
    groups = groupingMarbles()

    for group in groups:
        length = len(group)
        value = data[group[0][0]][group[0][1]]
        new_marbles.append(length)
        new_marbles.append(value)

    new_marbles += [0] * (n ** 2 - 1 - len(new_marbles))
    new_data = [[0]*n for _ in range(n)]
    x, y, d, t, i = xy, xy, 0, 0, 0

    while 1:
        t += dt[d]
        for _ in range(t):
            x, y = x + dx[d], y + dy[d]

            if (x, y) == (0, -1):
                return new_data
            new_data[x][y] = new_marbles[i]
            i += 1

        d = (d + 1) % 4


result = {1: 0, 2: 0, 3: 0}
for d, s in command:
    destroyMarbles(d, s)
    data = moveMarbles()

    while 1:
        count = burstMarbles()
        if tuple(count.values()) == (0, 0, 0):
            break

        for i in range(1, 4):
            result[i] += count[i]
        
        data = moveMarbles()
    
    data = transformMarbles()

print(result[1] + 2 * result[2] + 3 * result[3])