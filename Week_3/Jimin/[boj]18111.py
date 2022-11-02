'''
'마인크래프트'
'''
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
board = []

for i in range(N):
    board.append(list(map(int, input().split())))

answer_height = 0
answer_time = int(1e9)
for i in range(257):
    time = 0
    push = 0
    pull = 0
    for x in range(N):
        for y in range(M):
            if board[x][y] < i:
                push += i - board[x][y]
            elif board[x][y] > i:
                pull += board[x][y] - i

    if push > pull+B:
        break
    else:
        time = push + pull * 2

    if time <= answer_time:
        answer_time = time
        answer_height = i

print(answer_time, answer_height)
