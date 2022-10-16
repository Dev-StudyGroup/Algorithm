from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
space = [[0 for _ in range(N)] for _ in range(N)]
dic = defaultdict(list)


def locate(student):
    like, empty = 0, -1
    loc = []
    for i in range(N):
        for j in range(N):
            if space[i][j]:
                continue
            like_cnt = 0
            empty_cnt = 0
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
                    if space[nx][ny] in dic[student]:
                        like_cnt += 1
                    if space[nx][ny] == 0:
                        empty_cnt += 1
            if like < like_cnt:
                like = like_cnt
                loc = [[i,j,empty_cnt]]
            elif like == like_cnt:
                loc.append([i,j,empty_cnt])

    if len(loc) == 1:
        space[loc[0][0]][loc[0][1]] = student
    elif len(loc) > 1:
        loc.sort(key = lambda x:-x[2])
        space[loc[0][0]][loc[0][1]] = student


for _ in range(N * N):
    student_no, a, b, c, d = map(int, input().split())
    dic[student_no] = [a, b, c, d]
    locate(student_no)

res = 0
for i in range(N):
    for j in range(N):
        satified = 0
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]
            if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
                if space[nx][ny] in dic[space[i][j]]:
                    satified += 1
        if satified:
            res += pow(10,satified-1)
print(res)