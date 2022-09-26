"""
부녀회장이 될테야
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
apart = [[0] * 15 for _ in range(15)]

for i in range(15):
    apart[0][i] = i + 1

for i in range(1, 15):
    for j in range(15):
        apart[i][j] = sum([apart[i - 1][x] for x in range(j + 1)])

t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    print(apart[k][n-1])
