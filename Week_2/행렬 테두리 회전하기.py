"""
Dev Matching: 행렬 테두리 회전하기
"""

def solution(rows, columns, queries):
    answer = []
    arr = [[0 for i in range(columns)] for j in range(rows)]
    t = 1
    for row in range(rows):
        for col in range(columns):
            arr[row][col] = t
            t += 1

    for r1, c1, r2, c2 in queries:
        temp = arr[r1-1][c1-1] 
        mini = temp
        # for문 -> 좌하우상 순서로 이동
        for i in range(r1-1, r2-1): # 왼쪽 세로
            tmp = arr[i+1][c1-1]
            arr[i][c1-1] = tmp
            mini = min(tmp, mini)
        for i in range(c1-1, c2-1): # 하단 가로
            tmp = arr[r2-1][i+1]
            arr[r2-1][i] = tmp
            mini = min(tmp, mini)
        for i in range(r2-1, r1-1, -1): # 오른쪽 세로
            tmp = arr[i-1][c2-1]
            arr[i][c2-1] = tmp
            mini = min(tmp, mini)
        for i in range(c2-1,c1-1, -1): # 상단 가로
            tmp = arr[r1-1][i-1]
            arr[r1-1][i] = tmp
            mini = min(tmp, mini)
        arr[r1-1][c1] = temp
        answer.append(mini)
    return answer
