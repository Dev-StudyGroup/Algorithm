'''
'상어 초등학교'
'''
N = int(input())
board = [[0 for i in range(N)] for i in range(N)]
dic = {}

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(N*N):
    a, b, c, d, e = map(int, input().split())
    dic[a] = [b, c, d, e]

for x in dic:
    like = 0
    none = 0
    idx = [20, 20]
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                continue
            like_cnt = 0
            none_cnt = 0
            for k in range(4):
                mx = i + dx[k]
                my = j + dy[k]
                if mx < 0 or mx >= N or my < 0 or my >= N:
                    continue
                elif board[mx][my] == 0:
                    none_cnt += 1
                elif board[mx][my] in dic[x]:
                    like_cnt += 1
            if like_cnt > like:
                like = like_cnt
                none = none_cnt
                idx = [i, j]
            elif like_cnt == like and none_cnt > none:
                none = none_cnt
                idx = [i, j]
            elif like_cnt == like and none_cnt == none and i < idx[0]:
                idx = [i, j]
            elif like_cnt == like and none_cnt == none and i == idx[0] and j < idx[1]:
                idx = [i, j]

    board[idx[0]][idx[1]] = x

answer = 0
for i in range(N):
    for j in range(N):
        num = board[i][j]
        cnt = 0
        for k in range(4):
            mx = i + dx[k]
            my = j + dy[k]
            if mx < 0 or mx >= N or my < 0 or my >= N:
                continue
            if board[mx][my] in dic[num]:
                cnt += 1
        if cnt == 0 or cnt == 1:
            answer += cnt
        elif cnt == 2:
            answer += 10
        elif cnt == 3:
            answer += 100
        elif cnt == 4:
            answer += 1000

print(answer)
