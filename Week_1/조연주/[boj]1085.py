"""
직사각형에서 탈출
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
x, y, w, h = map(int, input().split())
up = h - y
down = y
left = x
right = w - x
print(min(up, down, left, right))
