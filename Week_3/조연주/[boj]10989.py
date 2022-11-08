"""
수 정렬하기 3
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
import sys

n = int(sys.stdin.readline()) # input() 사용 시 시간초과
l = [0] * 10001

for i in range(n):
    a = int(sys.stdin.readline())
    l[a] += 1

for i in range(10001):
    for j in range(l[i]):
        print(i)
