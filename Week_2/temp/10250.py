"""
10250: ACM 호텔
"""

# W개의 방, H층 건물 -> 너비 W, 높이 H
# 방 번호 : YXX, YYXX -> Y/YY 층수, XX 호수
# 걷는 거리가 가장 짧도록 -> 작은 호수
# 걷는 거리가 같으면 낮은 층

t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())

    arc = n // h + 1
    if n % h == 0:
        floor = h
        arc -= 1
    else:
        floor = n % h
    print(floor * 100 + arc)
