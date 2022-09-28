"""
OX퀴즈
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
t = int(input())

for _ in range(t):
    result = 0
    score = 1
    ox = list(input())
    for p in ox:
        if p == 'O':
            result += score
            score += 1
        else:
            score = 1
    print(result)
