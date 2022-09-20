
from itertools import product
def make_chess(n, m):
    """
    product 함수를 이용하여 n*m 보드 크기에서 8*8 chess판의 조합을 모두 구함

    """
    if n == 8 and m == 8:
        return [[[0,8],[0,8]]]
    x_cnt = n-7
    y_cnt = m-7

    x_ls = [[a,a+8] for a in range(0, x_cnt)]
    y_ls = [[a,a+8] for a in range(0, y_cnt)]

    ret_ls = []
    for r in product(x_ls, y_ls):
        p = [r[0],r[1]]
        if p not in ret_ls:
            ret_ls.append(p)
    return ret_ls


n, m = map(int, input().split())
board = []
for _ in range(0, n):
    board.append(list(input()))


chess = make_chess(n, m) # 보드에서 만들 수 있는 체스의 경우의 수
paint = [] # 각 경우마다 색칠한 정사각형의 개수
for idx in chess:
    start_x = idx[0][0]
    end_x = idx[0][1]
    start_y = idx[1][0]
    end_y = idx[1][1]

    f_w_cnt = 0
    f_b_cnt = 0
    # 잘라낸 보드의 크기는 8 * 8이다.
    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            temp_rect = board[i][j]
            if (i + j) % 2 == 0:
                if board[i][j] != 'W':
                    f_w_cnt += 1
                if board[i][j] != 'B':
                    f_b_cnt += 1
            else:
                if board[i][j] != 'B':
                    f_w_cnt += 1
                if board[i][j] != 'W':
                    f_b_cnt += 1
    paint.append(f_w_cnt)
    paint.append(f_b_cnt)

print(min(paint))




