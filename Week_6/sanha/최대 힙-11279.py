import heapq as hq
import sys

input = sys.stdin.readline

N = int(input())
pq = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if not pq:
            print(0)
        else:
            print(-hq.heappop(pq))
        continue
    hq.heappush(pq, -x)
