import heapq
import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N = int(input())
    q = []
    for _ in range(N):
        n = int(input())
        if n:
            heapq.heappush(q, n)
        else:
            if len(q):
                print(heapq.heappop(q))
            else:
                print(0)
