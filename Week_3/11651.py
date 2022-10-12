"""
11651: 좌표 정렬하기2
"""
import sys
n = int(sys.stdin.readline())
crd = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

crd.sort()
crd.sort(key = lambda x: x[1])

for i in crd:
    print(i[0], i[1])

    