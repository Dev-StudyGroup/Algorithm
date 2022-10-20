N = int(input())
NN = N ** 2
students = [list(map(int, input().split())) for _ in range(NN)]
G = [[0] * N for _ in range(N)]
dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_boundary(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

for student in students:
    tmp = []
    for x in range(N):
        for y in range(N):
            blanks = 0
            likes = 0
            if G[x][y] == 0:
                for dx, dy in zip(dxs, dys):
                    nx = x + dx
                    ny = y + dy
                    if in_boundary(nx, ny):
                        if G[nx][ny] == 0:
                            blanks += 1
                        if G[nx][ny] in student[1:]:
                            likes += 1
                tmp.append((likes, blanks, x, y))
    tmp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    G[tmp[0][2]][tmp[0][3]] = student[0]

students.sort()
answer = 0
for x in range(N):
    for y in range(N):
        if G[x][y] != 0:
            cnt = 0
            for dx, dy in zip(dxs, dys):
                nx = x + dx
                ny = y + dy
                if in_boundary(nx, ny):
                    if G[nx][ny] in students[G[x][y] - 1]:
                        cnt += 1
            if cnt == 0:
                continue
            answer += 10 ** (cnt - 1)
print(answer)
