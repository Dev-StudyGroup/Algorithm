"""
마법사 상어와 파이어볼
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
n, m, k = map(int, input().split())
ball= []
result = 0
board = [[[] for _ in range(n)] for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(m):
    r, c, m, s, d = list(map(int, input().split()))
    ball.append([r - 1, c - 1, m, s, d])

for _ in range(k):
    while ball:
        ri, ci, mi, si, di = ball.pop(0)
        nx = (ri + si * dx[di]) % n
        ny = (ci + si * dy[di]) % n
        board[nx][ny].append([mi, si, di])

    for i in range(n):
        for j in range(n):
            if len(board[i][j]) > 1:
                weight = 0
                speed = 0
                odd = 0
                even = 0
                balls = len(board[i][j])

                while board[i][j]:
                    m, s, d = board[i][j].pop(0)
                    weight += m
                    speed += s
                    if d % 2:
                        odd += 1
                    else:
                        even += 1
                
                divide_weight = weight // 5
                divide_speed = speed // balls
                divide_direction = [1, 3, 5, 7]
                if odd == balls or even == balls:
                    divide_direction = [0, 2, 4, 6]

                if divide_weight:
                    for x in divide_direction:
                        ball.append([i, j, divide_weight, divide_speed, x])
            elif len(board[i][j]) == 1:
                ball.append([i, j] + board[i][j].pop())

print(sum([b[2] for b in ball]))
