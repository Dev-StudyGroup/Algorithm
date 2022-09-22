'''
'체스판 다시 칠하기'
'''
N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(input())

startW = ['' for _ in range(N)]
startB = ['' for _ in range(N)]

for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            if j % 2 == 0:
                startW[i] += 'W'
                startB[i] += 'B'
            else:
                startW[i] += 'B'
                startB[i] += 'W'
        else:
            if j % 2 == 0:
                startW[i] += 'B'
                startB[i] += 'W'
            else:
                startW[i] += 'W'
                startB[i] += 'B'

answer = 999
for i in range(N-7):
    for j in range(M-7):
        cnt1 = 0
        cnt2 = 0
        for x in range(8):
            for y in range(8):
                if startW[x][y] != board[i+x][j+y]:
                    cnt1 += 1
                if startB[x][y] != board[i + x][j + y]:
                    cnt2 += 1
        answer = min(cnt1, cnt2, answer)

print(answer)