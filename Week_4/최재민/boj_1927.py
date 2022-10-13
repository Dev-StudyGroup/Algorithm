import heapq
import sys

n = int(input())
arr = []

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        if not arr:
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, num)
