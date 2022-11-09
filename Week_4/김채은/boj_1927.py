import heapq
import sys

input = sys.stdin.readline

n = int(input().strip())

arr = []

for _ in range(n):
    number = int(input())

    if number == 0:
        if not arr:
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, number)
