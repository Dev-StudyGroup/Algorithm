'''
'행렬 테두리 회전하기'
'''
def solution(rows, columns, queries):
    answer = []
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    board = [[0 for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            board[i][j] = i*columns + j+1

    for i in queries:
        x1, y1, x2, y2 = int(i[0])-1, int(i[1])-1, int(i[2])-1, int(i[3])-1
        x, y = x1, y1
        present = board[x][y]
        minimum = present
        move = 0
        while True:
            mx = x + dx[move]
            my = y + dy[move]
            if my > y2 or mx > x2 or my < y1:
                move += 1
                continue
            if mx < x1:
                break
            temp = board[mx][my]
            board[mx][my] = present
            present = temp
            minimum = min(minimum, temp)
            x, y = mx, my

        answer.append(minimum)

    return answer

# print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
# print(solution(100, 97, [[1,1,100,97]]))
