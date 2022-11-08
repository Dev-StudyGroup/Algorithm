"""
1780: 종이의 개수
* 분할정복
"""

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
minus, plus, zero = 0, 0, 0

def count(x, y, n):
    global minus, plus, zero 

    num = board[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if board[i][j] != num:
                for k in range(3):
                    for l in range(3):
                        count(x + k*n//3, y + l*n//3, n // 3)
                return

    if num == -1:
        minus += 1
    elif num == 0:
        zero += 1
    else:
        plus += 1

count(0,0,n)
print(minus)
print(zero)
print(plus)

