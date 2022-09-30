'''
'컨베이어 벨트 위의 로봇'
'''
n, k = map(int, input().split())
board = list(map(int, input().split()))
board[n:2*n] = reversed(board[n:2*n])

robot = [0 for i in range(n)]

answer = 0      # 단계 세기

while True:
    answer += 1

    # 1. 벨트 회전
    temp1 = board[n]
    temp2 = board[n-1]
    next_r = 0
    for i in range(2*n):
        if i < n-1:
            next_r, robot[i] = robot[i], next_r
        elif i == n-1:
            robot[i] = 0

        if i < n:
            if i == 0:
                next_b, board[i] = board[i], temp1
            else:
                next_b, board[i] = board[i], next_b
        else:
            if i == 2*n-1:
                board[i] = temp2
            else:
                board[i] = board[i+1]

    # 2. 로봇 이동
    for i in range(n-1, -1, -1):
        if i == n-1:
            robot[i] = 0
        else:
            if robot[i+1] == 0 and robot[i] == 1:
                if board[i+1] > 0:
                    robot[i+1], robot[i] = 1, 0
                    board[i+1] -= 1

    # 3. 로봇 올리기
    if board[0] != 0:
        robot[0] = 1
        board[0] -= 1

    # 4. 내구도가 0인 칸의 개수가 k개 이상이면 종료
    cnt = 0
    for i in range(2*n):
        if board[i] == 0:
            cnt += 1

    if cnt >= k:
        break

print(answer)