def rotate(array, x1, y1, x2, y2):
    rightup = array[x1][y2]
    min_num = rightup
    for i in range(y2, y1, -1):
        array[x1][i] = array[x1][i-1]
        if array[x1][i] < min_num:
            min_num = array[x1][i]
    for i in range(x1, x2):
        array[i][y1] = array[i+1][y1]
        if array[i][y1] < min_num:
            min_num = array[i][y1]
    for i in range(y1, y2):
        array[x2][i] = array[x2][i + 1]
        if array[x2][i] < min_num:
            min_num = array[x2][i]
    for i in range(x2, x1+1, -1):
        array[i][y2] = array[i-1][y2]
        if array[i][y2] < min_num:
            min_num = array[i][y2]
    array[x1+1][y2] = rightup
    return min_num


def solution(rows, columns, queries):
    array = [[columns * r + c for c in range(1, columns + 1)] for r in range(rows)]
    answer = []
    for x1, y1, x2, y2 in queries:
        answer.append(rotate(array, x1 - 1, y1 - 1, x2 - 1, y2 - 1))
    return answer

solution(100,97,[[1,1,100,97]])