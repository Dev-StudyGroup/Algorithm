'''
'마법사 상어와 파이어볼'
'''
N, M, K = map(int, input().split())

board = {}      # 각 좌표별 파이어볼 정보 담는 dic(4*4일 경우 2차원 [1,0] 좌표를 5로 생각)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(M):
    r, c, m, s, d = map(int, input().split())
    board[(r-1)*N+c] = [[m, s, d]]

for k in range(K):
    new_board = {}

    # 1단계
    for i in board:
        for j in board[i]:
            m, s, d = j[0], j[1], j[2]

            # 1차원 좌표를 2차원 좌표로 변경
            if i % N == 0:
                r = i // N - 1
                c = N - 1
            else:
                r = i // N
                c = i % N - 1

            mr = ((r + dx[d] * s) % N)
            if mr < 0:
                mr + 4
            mc = (c + dy[d] * s) % N

            # 2차원 좌표를 1차원 좌표로 변경
            dd = mr * N + mc + 1

            if dd in new_board:
                new_board[dd].append([m, s, d])
            else:
                new_board[dd] = [[m, s, d]]

    board = new_board       # 주소 확인 필요
    new_board = {}

    # 2단계
    for i in board:
        if len(board[i]) > 1:
            sumM = 0
            sumS = 0
            resultD = [0, 0]
            ballD = 0

            for j in board[i]:
                m, s, d = j[0], j[1], j[2]
                sumM += m
                sumS += s
                if d % 2 == 0:
                    resultD[0] += 1
                elif d % 2 == 1:
                    resultD[1] += 1

            resultM = sumM // 5
            resultS = sumS // len(board[i])
            if resultD[0] == 0 or resultD[1] == 0:
                ballD = 0
            else:
                ballD = 1

            # 파이어볼 네개로 쪼개기
            if resultM == 0:
                continue
            for j in range(4):
                if i in new_board:
                    new_board[i].append([resultM, resultS, ballD])
                else:
                    new_board[i] = [[resultM, resultS, ballD]]
                ballD += 2
        else:
            if i in new_board:
                new_board[i].append(board[i])
            else:
                new_board[i] = board[i]
    board = new_board

answer = 0
for i in board:
    for j in board[i]:
        answer += j[0]

print(answer)