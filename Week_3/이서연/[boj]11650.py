'''
좌표 정렬하기

- 문제 요약
2차원 평면 위의 점 N개가 주어진다.
좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램

- 입력 조건
첫째 줄에 점의 개수 N(1 <= N <= 100,000)이 주어진다.
둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다.
(-100,000 <= xi, yi <= 100,000)
좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

- 출력 조건
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력
'''
import sys
n = int(sys.stdin.readline())
point = []
for _ in range(n):
    point.append(list(map(int, sys.stdin.readline().split())))
point.sort(key= lambda x: (x[0], x[1])) # x좌표 기준 정렬 -> y좌표 기준 정렬

for p in point:
    print(p[0],p[1])
    