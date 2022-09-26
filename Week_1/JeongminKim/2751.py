"""

    N개의 수가 주어짐
    오름차순으로 정렬

"""
import sys

N = int(sys.stdin.readline())

ls = []

for _ in range(N):
    ls.append(int(sys.stdin.readline()))

ls.sort(reverse=False)

for i in ls:
    print(i)
