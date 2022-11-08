# [BOJ] 1085 직사각형에서 탈출

x, y, w, h = map(int, input().split())

answer = min(abs(x-w), abs(y-h), x, y)
print(answer)
