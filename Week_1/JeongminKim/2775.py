"""

    거주 조건 a층의 b호에 살려면 a-1층의 1~b까지 사람들의 수의 합만큼 사람을 데려와 살아야함

    주어지는 양의 정수 k, n에 대해
    k층 n호에는 몇명이 살고있는지 출력하라

    아파트는 0층부터 있고 각층에는 1호부터 있음

"""
import sys

t = int(sys.stdin.readline())
for _ in range(t):

    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    apart = []
    for _ in range(k + 1):
        apart.append([i for i in range(0, n + 1)])
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            apart[i][j] = sum(apart[i - 1][:j + 1])

    print(apart[k][n])
