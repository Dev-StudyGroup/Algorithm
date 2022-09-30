"""
수 정렬하기 2
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
import sys

n = int(input())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()
print(*nums, sep='\n')
