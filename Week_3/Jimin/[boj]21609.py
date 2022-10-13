'''
'상어 중학교'
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, N, color):
    global cnt, visited_list, rainbow
    visited[x][y] = 1
    visited_list.append([x, y])
    if board[x][y] == 0:
        temp.append([x, y])
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if mx < 0 or mx >= N or my < 0 or my >= N or visited[mx][my] == 1:
            continue
        if board[mx][my] == color or board[mx][my] == 0:
            if board[mx][my] == 0:
                rainbow += 1
            cnt += 1
            dfs(mx, my, N, color)

def gravity(N):
    for i in range(N):
        next_idx = [-1, -1]
        for j in range(N-1, -1, -1):
            if board[j][i] == -2:
                if next_idx == [-1, -1]:
                    next_idx = [j, i]
            elif board[j][i] == -1:
                next_idx = [-1, -1]
            else:
                if next_idx != [-1, -1]:
                    board[next_idx[0]][next_idx[1]] = board[j][i]
                    board[j][i] = -2
                    next_idx[0] -= 1
    return

def turn(array):
    array = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            array[N-1-j][i] = board[i][j]
    return array

delete_list = []
answer = 0
while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    temp = []
    max_cnt = 0
    max_rainbow = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] != -1 and board[i][j] != -2 and board[i][j] != 0 and visited[i][j] == 0:
                cnt = 1
                rainbow = 0
                visited_list = []
                dfs(i, j, N, board[i][j])
                if max_cnt < cnt or (max_cnt == cnt and max_rainbow <= rainbow):
                    max_cnt = cnt
                    max_rainbow = rainbow
                    delete_list = visited_list
                for k in temp:                      # 0인 부분 방문 초기화
                    visited[k[0]][k[1]] = 0


    if max_cnt == 1 or max_cnt == 0:
        break
    for i in delete_list:
        board[i[0]][i[1]] = -2

    answer += max_cnt ** 2
    gravity(N)
    board = turn(board)
    gravity(N)

print(answer)
