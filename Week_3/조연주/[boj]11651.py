"""
좌표 정렬하기 2
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
import sys

n = int(sys.stdin.readline())
coordination = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    coordination.append((x, y))

coordination.sort(key=lambda x : (x[1], x[0]))

for i in range(n):
    print(coordination[i][0], coordination[i][1])
