"""

    좌표룰
    x좌표 증가하는 순으로
    x좌표가 같으면 y좌표가 증가하는 순서로 정렬한다.

"""
import sys

N = int(input())
coords = []
for _ in range(N):
    coords.append(list(map(int, sys.stdin.readline().split())))

coords.sort(key=lambda x: [x[0], x[1]], reverse=False)

for c in coords:
    print(f'{c[0]} {c[1]}')
