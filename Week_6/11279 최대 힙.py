import sys
import heapq

input = sys.stdin.readline
if __name__ == "__main__":
    N = int(input())
    q = []
    for _ in range(N):
        x = int(input())
        if x > 0:
            heapq.heappush(q, -x)
            continue
        if x == 0:
            if len(q):
                print(-heapq.heappop(q))
                continue
            print(0)
