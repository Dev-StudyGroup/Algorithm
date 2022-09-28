"""
알람 시계
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
h, m = map(int, input().split())

if m >= 45:
    print(h, m - 45)
elif h > 0:
    print(h - 1, m + 15)
else:
    print(23, m + 15)