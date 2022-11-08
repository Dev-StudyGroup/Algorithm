'''
'마법사 상어와 블리자드'
'''
N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
shark = [N//2, N//2]

movement = []
n, m = shark
mode_x = [0, 1, 0, -1]
mode_y = [-1, 0, 1, 0]
mode = 0                        # 0:왼쪽, 1:아래, 2:오른쪽, 3:위
mode_distance = [1, 1, 2, 2]
while True:
    if n == 0 and m == 0:
        break
    for i in range(mode_distance[mode]):
        mn = n + mode_x[mode]
        mm = m + mode_y[mode]
        n, m = mn, mm
        if n == 0 and m == 0:
            break
        movement.append([n, m])
    mode_distance[mode] += 2
    mode = (mode + 1) % 4

movement.append([0, 0])


def move_bomb():        # 구슬 폭발 함수
    result = 0          # 폭발한 것에 대한 점수 기록
    while True:
        end = 0
        color = board[movement[0][0]][movement[0][1]]
        idx = []
        for i in range(len(movement)):
            x, y = movement[i]
            if board[x][y] == 0:
                continue
            elif board[x][y] == color:
                idx.append([x, y])
            else:
                if len(idx) >= 4:
                    end = 1
                    for j in idx:
                        board[j[0]][j[1]] = 0
                    result += len(idx) * color
                idx = [[x, y]]
                color = board[x][y]
        if end == 0:
            break

    if len(idx) >= 4:       # 다 돌고 끝에 남은 부분 검사
        end = 1
        for j in idx:
            board[j[0]][j[1]] = 0
        result += len(idx) * color

    return result           # 폭발한 것에 대한 점수 리턴

def change():               # 구슬 변화 함수
    new_board = [[0 for _ in range(N)] for _ in range(N)]
    color = 0
    start = 0
    cnt = 0
    temp = 0
    for i in range(len(movement)):
        x, y = movement[i]
        if board[x][y] == 0:
            continue
        if start == 0:
            color = board[x][y]
            cnt += 1
            start = 1
            continue
        if temp >= len(movement):
            break
        tempX, tempY = movement[temp]
        if board[x][y] == color:
            cnt += 1
        else:
            new_board[tempX][tempY] = cnt
            if temp+1 < len(movement):
                tempX, tempY = movement[temp+1]
                new_board[tempX][tempY] = color
            else:
                break
            color = board[x][y]
            cnt = 1
            temp += 2

    if temp < len(movement):                # 다 돌고 끝에 남은 부분 검사
        tempX, tempY = movement[temp]
        new_board[tempX][tempY] = cnt
    if temp + 1 < len(movement):
        tempX, tempY = movement[temp + 1]
        new_board[tempX][tempY] = color

    return new_board                        # 변화한 구슬판 리턴

answer = 0
for i in range(M):
    d, s = map(int, input().split())
    x, y = shark
    for j in range(s):
        x = x + dx[d-1]
        y = y + dy[d-1]
        board[x][y] = 0
    answer += move_bomb()
    if i == M-1:
        break
    board = change()

print(answer)
