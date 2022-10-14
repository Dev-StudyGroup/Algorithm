data = {}
n = int(input())
for _ in range(n**2):
    s, f1, f2, f3, f4 = map(int, input().split())
    data[s] = [f1, f2, f3, f4]

seats = [[0]*n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for student, friends in list(data.items()):
    result = (0, 0, -n+1, -n+1)
    for x in range(n):
        for y in range(n):
            if seats[x][y]:
                continue
            friend_cnt, empty_cnt = 0, 0
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if seats[nx][ny] == 0:
                    empty_cnt += 1
                    continue
                if seats[nx][ny] in friends:
                    friend_cnt += 1
                    continue
            result = max(result, (friend_cnt, empty_cnt, -x, -y))
    x, y = -result[-2], -result[-1]
    seats[x][y] = student

answer = 0
for x in range(n):
    for y in range(n):
        student = seats[x][y]
        count = 0
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if seats[nx][ny] in data[student]:
                count += 1
        if count == 0:
            continue
        answer += 10**(count-1)

print(answer)