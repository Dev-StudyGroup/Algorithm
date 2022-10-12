"""
상어 초등학교
"""

"""
N*N 크기의 교실, 학생의 수는 N^2
(r, c) : r행 c열

1. 비어있는 칸 중 좋아하는 학생이 제일 많이 인접한 칸으로 
2. 1을 만족하는 칸이 여러개이면, 인접한 칸이 많이 비어있는 곳으로
3. 2를 만족하는 칸이 여러개이면, 행의 번호가 가장 작은 -> 열의 번호가 가장 작은 곳으로
"""
import sys

n = int(sys.stdin.readline())
arr = [[0] * n for j in range(n)]
std = [list(map(int, input().split())) for _ in range(n**2)]
dr = [-1, 0, 1, 0] # 행 -> 상우하좌
dc = [0, 1, 0, -1]

for i in range(n ** 2):
    tmp = []
    for r in range(n):
        for c in range(n):
            if arr[r][c] == 0:
                like, empty = 0, 0
                for j in range(4):
                    nr = r + dr[j]
                    nc = c + dc[j]
                    if nr < 0 or nr >= n or nc < 0 or nc >= n:
                        continue
                    if arr[nr][nc] in std[i][1:]:
                        like += 1
                    if arr[nr][nc] == 0:
                        empty += 1
                tmp.append([like, empty, r, c])
    tmp.sort(key = lambda x: ((-x[0], -x[1], x[2], x[3])))
    arr[tmp[0][2]][tmp[0][3]] = std[i][0]

result = 0
std.sort()

for i in range(n):
    for j in range(n):
        ans = 0
        for k in range(4):
            nr, nc = i + dr[k], j + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] in std[arr[i][j]-1]:
                    ans += 1
        if ans != 0:
            result += 10 ** (ans-1)
print(result)


