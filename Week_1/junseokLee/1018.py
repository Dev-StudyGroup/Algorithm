n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(input())
count = 0
result = 65


def check(a, b):
    global count
    color = 'W'
    res = 65
    for k in range(2):
        count = 0
        if color == 'W':
            color = 'B'
        else:
            color = 'W'
        for i in range(a, a + 8):
            if color == 'W':
                color = 'B'
            else:
                color = 'W'
            for j in range(b, b + 8):
                if (j % 2 == 0 and board[i][j] != color) or (j % 2 == 1 and board[i][j] == color):
                    count += 1
        res = min(res, count)
    return res


for i in range(n - 7):
    for j in range(m - 7):
        result = min(result, check(i, j))
print(result)
