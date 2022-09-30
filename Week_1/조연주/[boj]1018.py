"""
체스판 다시 칠하기
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
n, m = map(int, input().split())
rect = [[str(x) for x in input()]for y in range(n)]
new_min = 64

for i in range(n - 7):
    for j in range(m - 7):
        b = 0
        w = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0 :
                    if rect[k][l] != 'W':
                        w += 1
                    if rect[k][l] != 'B':
                        b += 1
                else:
                    if rect[k][l] != 'B':
                        w += 1
                    if rect[k][l] != 'W':
                        b += 1
        new_min = min(new_min, b, w)
        
print(new_min)
