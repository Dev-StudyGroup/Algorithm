"""
18111: 마인크래프트
"""

"""
집터 땅 고르기 작업 -> 세로 N, 가로 M 크기의 집터
집터 맨 왼쪽 위의 좌표는 (0,0) -> 땅 높이를 일정하게 바꾸는 것이 목표
- 좌표(i,j)의 맨 위 블록을 제거해 인벤토리에 넣는다. (2s) 제거
- 인벤토리에서 블록 하나를 꺼내어 좌표(i,j)의 가장 위에 놓는다. (1s) 쌓기 
"""
import sys
from collections import Counter

n, m, b = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
height, avg = 256, b
fast = sys.maxsize

for i in range(n):
    for j in range(m):
        avg += arr[i][j]
avg = avg // (n*m)

for floor in range(avg, -1, -1):
    t = 0
    for i in range(n):
        for j in range(m):
            count = arr[i][j] - floor
            t += count * 2 if count > 0 else -count
    if t < fast:
        fast = t
        height = floor
    else: break

print(fast, height)

