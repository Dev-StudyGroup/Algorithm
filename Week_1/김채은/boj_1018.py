# [BOJ] 1018 체스판 다시 칠하기
# Time Taken: 43m

n, m = map(int, input().split())
chess = [list(input()) for _ in range(n)]

INF = 10000

global answer
answer = INF

def paint(index):
    colors = ['W', 'B']
    for i in range(n):
        for j in range(m):
            if chess[i][j] != colors[index]:
                painted[i][j] = 1
            index = (index + 1) % 2
        if m % 2 == 0:    
            index = (index + 1) % 2

def count(i, j):
    _sum = 0

    for a in range(8):
        for b in range(8):
            _sum += painted[i+a][j+b]

    return _sum

def getMin():
    global answer
    for i in range(n):
        for j in range(m):
            if n - i >= 8 and m - j >= 8:
                answer = min(answer, count(i, j))

for index in range(2):
    painted = [[0] * m for _ in range(n)]
    paint(index)
    getMin()    

print(answer)
