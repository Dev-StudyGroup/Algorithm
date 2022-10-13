"""

    N개의 수가 주어졌을때 오름차순으로 정렬하는 프로그램을 작성하시요

"""

from collections import defaultdict
import sys

N = int(input())
numbers = defaultdict(int)
for _ in range(N):
    value = int(sys.stdin.readline())
    numbers[value] += 1
numbers = sorted(numbers.items(), key=lambda x: x[0], reverse=False)
for key, value in numbers:
    for _ in range(value):
        print(key)
