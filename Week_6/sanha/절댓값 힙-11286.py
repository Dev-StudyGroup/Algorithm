import sys
import heapq as hq

input = sys.stdin.readline

N = int(input())
pq = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if not pq:
            print(0)
        else:
            print(hq.heappop(pq)[1])
        continue
    hq.heappush(pq, (abs(x), x))
